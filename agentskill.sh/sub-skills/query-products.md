# Query Products

Validated patterns for the Shopify Admin GraphQL API (2026-01).

## Basic Product List

```graphql
{
  products(first: 10) {
    edges {
      node {
        id
        title
        handle
        status
        variants(first: 5) {
          edges {
            node {
              id
              price
              compareAtPrice
              availableForSale
              inventoryQuantity
            }
          }
        }
        featuredImage {
          url
          altText
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

## Cursor-Based Pagination

```graphql
{
  products(first: 10, after: "CURSOR_STRING") {
    edges {
      node {
        id
        title
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

## Filter by Tag or Status

```graphql
{
  products(first: 20, query: "tag:organic status:active") {
    edges {
      node {
        id
        title
        tags
      }
    }
  }
}
```

## With Metafields

```graphql
{
  products(first: 10) {
    edges {
      node {
        id
        title
        metafields(identifiers: [
          { namespace: "custom", key: "origin" },
          { namespace: "custom", key: "roast_level" }
        ]) {
          namespace
          key
          value
        }
      }
    }
  }
}
```

## Notes

- Use `query:` filter string to narrow results before cursor pagination
- Request only the fields you need — GraphQL query cost scales with field count
- For > 250 products, switch to `bulkOperationRunQuery` mutation
- `availableForSale` is the reliable stock indicator; `inventoryQuantity` requires `read_inventory` scope
