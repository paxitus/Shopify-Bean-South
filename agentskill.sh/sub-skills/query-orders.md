# Query Orders

Validated patterns for the Shopify Admin GraphQL API (2026-01).
Requires `read_orders` scope.

## Basic Order List

```graphql
{
  orders(first: 10, sortKey: CREATED_AT, reverse: true) {
    edges {
      node {
        id
        name
        createdAt
        displayFinancialStatus
        displayFulfillmentStatus
        totalPriceSet {
          shopMoney {
            amount
            currencyCode
          }
        }
        customer {
          email
          firstName
          lastName
        }
        lineItems(first: 5) {
          edges {
            node {
              title
              quantity
              originalUnitPriceSet {
                shopMoney {
                  amount
                }
              }
            }
          }
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

## Filter by Date Range or Status

```graphql
{
  orders(
    first: 50
    query: "created_at:>2026-01-01 financial_status:paid"
  ) {
    edges {
      node {
        id
        name
        displayFinancialStatus
      }
    }
  }
}
```

## Common Query Filters

- `financial_status:paid` / `unpaid` / `refunded`
- `fulfillment_status:fulfilled` / `unfulfilled`
- `created_at:>DATE` / `updated_at:>DATE`
- `tag:wholesale`

## Notes

- Use `name` (e.g. `#1001`) for human-readable order numbers; `id` is the GID
- `totalPriceSet` uses `MoneyBag` type — always request `shopMoney` for store currency
- For bulk export of orders use `bulkOperationRunQuery` — avoids pagination limits
- Requires both `read_orders` scope AND the store must grant protected customer data access for `customer` fields
