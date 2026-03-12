# App Development Reference

Guide for building Shopify apps with OAuth, GraphQL, webhooks, and billing.

## OAuth Flow

### Step 1 — Redirect to Shopify Authorization

```
https://{shop}/admin/oauth/authorize
  ?client_id={API_KEY}
  &scope=read_products,write_products
  &redirect_uri=https://yourapp.com/auth/callback
  &state={NONCE}
```

### Step 2 — Exchange Code for Access Token

```javascript
const response = await fetch(`https://${shop}/admin/oauth/access_token`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    client_id: process.env.SHOPIFY_API_KEY,
    client_secret: process.env.SHOPIFY_API_SECRET,
    code: req.query.code,
  }),
});
const { access_token } = await response.json();
```

Store the token securely — see `sub-skills/security.md`.

## GraphQL Admin API

Base URL: `https://{shop}/admin/api/2026-01/graphql.json`

```javascript
async function shopifyGraphQL(shop, token, query, variables = {}) {
  const response = await fetch(
    `https://${shop}/admin/api/2026-01/graphql.json`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': token,
      },
      body: JSON.stringify({ query, variables }),
    }
  );

  const { data, errors } = await response.json();
  if (errors) throw new Error(JSON.stringify(errors));
  return data;
}
```

## Webhook Registration

```graphql
mutation {
  webhookSubscriptionCreate(
    topic: ORDERS_CREATE
    webhookSubscription: {
      format: JSON
      callbackUrl: "https://yourapp.com/webhooks/orders/create"
    }
  ) {
    webhookSubscription {
      id
      topic
    }
    userErrors {
      field
      message
    }
  }
}
```

Common topics: `ORDERS_CREATE`, `ORDERS_UPDATED`, `PRODUCTS_CREATE`, `PRODUCTS_UPDATE`, `APP_UNINSTALLED`, `SHOP_UPDATE`

Always validate HMAC on incoming webhooks — see `sub-skills/security.md`.

## Billing API

### Create App Subscription

```graphql
mutation appSubscriptionCreate($name: String!, $returnUrl: URL!, $test: Boolean) {
  appSubscriptionCreate(
    name: $name
    returnUrl: $returnUrl
    test: $test
    lineItems: [{
      plan: {
        appRecurringPricingDetails: {
          price: { amount: 9.99, currencyCode: USD }
          interval: EVERY_30_DAYS
        }
      }
    }]
  ) {
    appSubscription {
      id
      status
    }
    confirmationUrl
    userErrors {
      field
      message
    }
  }
}
```

Redirect merchant to `confirmationUrl` to approve. Use `test: true` during development.

### One-Time Charge

```graphql
mutation {
  appPurchaseOneTimeCreate(
    name: "Premium Export"
    returnUrl: "https://yourapp.com/billing/callback"
    price: { amount: 4.99, currencyCode: USD }
    test: true
  ) {
    appPurchaseOneTime {
      id
      status
    }
    confirmationUrl
    userErrors { field message }
  }
}
```

## Product Mutations

### Create Product

```graphql
mutation productCreate($input: ProductInput!) {
  productCreate(input: $input) {
    product {
      id
      title
    }
    userErrors {
      field
      message
    }
  }
}
```

Variables:
```json
{
  "input": {
    "title": "Ethiopian Yirgacheffe",
    "descriptionHtml": "<p>Bright, floral, naturally processed.</p>",
    "productType": "Coffee",
    "tags": ["organic", "single-origin"],
    "variants": [
      {
        "price": "18.00",
        "inventoryManagement": "SHOPIFY",
        "inventoryPolicy": "DENY"
      }
    ]
  }
}
```

### Update Product

```graphql
mutation productUpdate($input: ProductInput!) {
  productUpdate(input: $input) {
    product { id title }
    userErrors { field message }
  }
}
```

Variables: `{ "input": { "id": "gid://shopify/Product/123", "title": "New Title" } }`

## Rate Limiting

Monitor `X-Shopify-Shop-Api-Call-Limit` response header (REST) or query cost in GraphQL response extensions:

```json
{
  "extensions": {
    "cost": {
      "requestedQueryCost": 10,
      "actualQueryCost": 8,
      "throttleStatus": {
        "maximumAvailable": 1000,
        "currentlyAvailable": 992,
        "restoreRate": 50
      }
    }
  }
}
```

Implement exponential backoff on 429 responses — see `sub-skills/api-usage.md`.
