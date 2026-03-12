"""
Shopify GraphQL utility — query templates, pagination, rate limiting.

Usage:
    from shopify_graphql import ShopifyGraphQL
    client = ShopifyGraphQL(shop="mystore.myshopify.com", token="shpat_xxx")
    products = client.all_products()
"""

import time
import json
import urllib.request
import urllib.error
from typing import Any, Generator


class ShopifyGraphQL:
    API_VERSION = "2026-01"

    def __init__(self, shop: str, token: str):
        self.endpoint = f"https://{shop}/admin/api/{self.API_VERSION}/graphql.json"
        self.headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": token,
        }

    def query(self, gql: str, variables: dict | None = None, retries: int = 3) -> dict:
        """Execute a GraphQL query with exponential backoff on rate limits."""
        payload = json.dumps({"query": gql, "variables": variables or {}}).encode()
        delay = 1.0

        for attempt in range(retries):
            req = urllib.request.Request(self.endpoint, data=payload, headers=self.headers, method="POST")
            try:
                with urllib.request.urlopen(req) as resp:
                    result = json.loads(resp.read())
                if "errors" in result:
                    raise RuntimeError(f"GraphQL errors: {result['errors']}")
                return result.get("data", {})
            except urllib.error.HTTPError as e:
                if e.code == 429 and attempt < retries - 1:
                    time.sleep(delay)
                    delay *= 2
                    continue
                raise

        raise RuntimeError("Max retries exceeded")

    def paginate(self, gql: str, path: str, variables: dict | None = None) -> Generator[dict, None, None]:
        """
        Paginate through a connection field.

        `path` is a dot-separated path to the connection in the response,
        e.g. "products" or "orders".

        The query MUST include `pageInfo { hasNextPage endCursor }` and
        accept an `$after: String` variable.
        """
        cursor = None
        while True:
            vars_ = {**(variables or {}), "after": cursor}
            data = self.query(gql, vars_)

            # Navigate to the connection node
            node = data
            for key in path.split("."):
                node = node[key]

            for edge in node["edges"]:
                yield edge["node"]

            page_info = node["pageInfo"]
            if not page_info["hasNextPage"]:
                break
            cursor = page_info["endCursor"]

    # ── Convenience methods ────────────────────────────────────────────────

    def all_products(self, batch: int = 50) -> list[dict]:
        gql = """
        query($after: String) {
          products(first: %d, after: $after) {
            edges {
              node {
                id
                title
                handle
                status
                variants(first: 5) {
                  edges { node { id price availableForSale } }
                }
              }
            }
            pageInfo { hasNextPage endCursor }
          }
        }
        """ % batch
        return list(self.paginate(gql, "products"))

    def all_orders(self, query_filter: str = "", batch: int = 50) -> list[dict]:
        gql = """
        query($after: String) {
          orders(first: %d, after: $after%s) {
            edges {
              node {
                id
                name
                createdAt
                displayFinancialStatus
                displayFulfillmentStatus
                totalPriceSet { shopMoney { amount currencyCode } }
              }
            }
            pageInfo { hasNextPage endCursor }
          }
        }
        """ % (batch, f', query: "{query_filter}"' if query_filter else "")
        return list(self.paginate(gql, "orders"))

    def set_product_metafield(self, product_id: str, namespace: str, key: str, value: str, type_: str = "single_line_text_field") -> dict:
        gql = """
        mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
          metafieldsSet(metafields: $metafields) {
            metafields { id namespace key value }
            userErrors { field message }
          }
        }
        """
        result = self.query(gql, {
            "metafields": [{
                "ownerId": product_id,
                "namespace": namespace,
                "key": key,
                "value": value,
                "type": type_,
            }]
        })
        errors = result.get("metafieldsSet", {}).get("userErrors", [])
        if errors:
            raise RuntimeError(f"Metafield errors: {errors}")
        return result
