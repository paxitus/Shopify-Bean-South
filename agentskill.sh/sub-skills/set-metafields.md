# Set Metafields

Validated patterns for the Shopify Admin GraphQL API (2026-01).
Requires `write_products` (or appropriate owner scope).

## Create / Update Metafield via Mutation

```graphql
mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields {
      id
      namespace
      key
      value
      type
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
  "metafields": [
    {
      "ownerId": "gid://shopify/Product/12345678",
      "namespace": "custom",
      "key": "origin",
      "value": "Colombia",
      "type": "single_line_text_field"
    },
    {
      "ownerId": "gid://shopify/Product/12345678",
      "namespace": "custom",
      "key": "roast_level",
      "value": "Medium",
      "type": "single_line_text_field"
    }
  ]
}
```

## Common Metafield Types

| Type | Use for |
|------|---------|
| `single_line_text_field` | Short strings (origin, roast level) |
| `multi_line_text_field` | Long descriptions, tasting notes |
| `rich_text_field` | Formatted text (JSON structure) |
| `integer` | Numeric values |
| `boolean` | True/false flags |
| `list.single_line_text_field` | Arrays of strings |
| `rating` | Star ratings (requires `scale_min`, `scale_max`) |
| `file_reference` | Images / files |

## Reading Metafields in Liquid (Theme Side)

```liquid
{{ product.metafields.custom.origin }}
{{ product.metafields.custom.roast_level.value }}
{{ product.metafields.custom.tasting_notes | newline_to_br }}
```

## Define Metafield Definitions First

Before setting values, create a metafield definition in the Shopify admin so the type is enforced and the field appears in the admin UI:

```graphql
mutation {
  metafieldDefinitionCreate(definition: {
    name: "Origin"
    namespace: "custom"
    key: "origin"
    type: "single_line_text_field"
    ownerType: PRODUCT
  }) {
    createdDefinition {
      id
    }
    userErrors {
      field
      message
    }
  }
}
```

## Notes

- `metafieldsSet` is idempotent — creates or updates based on owner + namespace + key
- Always check `userErrors` in the response
- Use `gid://shopify/Product/ID` format for `ownerId`
- Metafield definitions are optional but strongly recommended for type safety
