# Extensions Reference

Guide for building Shopify UI Extensions: Checkout, Admin, POS, and Shopify Functions.

## Checkout UI Extension

### Setup

```bash
shopify app generate extension --type checkout_ui_extension --name my-checkout-block
```

### Basic Component (React)

```jsx
import {
  reactExtension,
  Banner,
  BlockStack,
  Text,
  useCartLines,
  useTotalAmount,
} from '@shopify/ui-extensions-react/checkout';

export default reactExtension(
  'purchase.checkout.block.render',
  () => <MyExtension />
);

function MyExtension() {
  const lines = useCartLines();
  const total = useTotalAmount();

  return (
    <BlockStack>
      <Banner status="info">
        <Text>You have {lines.length} item(s)</Text>
      </Banner>
    </BlockStack>
  );
}
```

### Extension Targets

| Target | Location |
|--------|----------|
| `purchase.checkout.block.render` | Configurable block in checkout |
| `purchase.checkout.contact.render-after` | After contact form |
| `purchase.checkout.shipping-option-list.render-after` | After shipping options |
| `purchase.checkout.payment-method-list.render-after` | After payment methods |
| `purchase.thank-you.block.render` | Thank you page |
| `purchase.checkout.cart-line-item.render-after` | After each line item |

### Metafield Updates from Checkout

```jsx
import { useApplyMetafieldChange } from '@shopify/ui-extensions-react/checkout';

function GiftMessageInput() {
  const applyMetafield = useApplyMetafieldChange();

  return (
    <TextField
      label="Gift message"
      onChange={(value) => applyMetafield({
        type: 'updateMetafield',
        namespace: 'custom',
        key: 'gift_message',
        valueType: 'string',
        value,
      })}
    />
  );
}
```

## Admin UI Extension

### Admin Action (button in product/order page)

```bash
shopify app generate extension --type admin_action --name product-tagger
```

```jsx
import { useApi, AdminAction, BlockStack, Button, Text } from '@shopify/ui-extensions-react/admin';

export default function AdminActionExtension() {
  const { data, close } = useApi('admin.product-details.action.render');

  return (
    <AdminAction>
      <BlockStack>
        <Text>Product: {data.selected[0]?.id}</Text>
        <Button onPress={close}>Done</Button>
      </BlockStack>
    </AdminAction>
  );
}
```

### Admin Block (embedded panel in admin page)

```bash
shopify app generate extension --type admin_block --name product-info
```

Target: `admin.product-details.block.render`

## Shopify Functions

Functions run server-side on Shopify's infrastructure for discount/delivery/payment logic.

### Discount Function

```bash
shopify app generate extension --type function --name volume-discount
```

`src/run.js`:
```javascript
export function run(input) {
  const percentage = input.cart.attribute?.value
    ? parseFloat(input.cart.attribute.value)
    : 0;

  return {
    discounts: percentage > 0 ? [{
      targets: [{ orderSubtotal: { excludedVariantIds: [] } }],
      value: { percentage: { value: percentage.toString() } },
      message: `${percentage}% off your order`,
    }] : [],
    discountApplicationStrategy: 'FIRST',
  };
}
```

Function types: `discount`, `delivery_customization`, `payment_customization`, `fulfillment_constraints`

## POS UI Extension

```bash
shopify app generate extension --type pos_ui_extension --name pos-loyalty
```

Targets: `pos.home.tile.render`, `pos.home.modal.render`

## Configuration (`shopify.extension.toml`)

```toml
name = "My Checkout Block"
type = "ui_extension"
api_version = "2026-01"

[[extensions.targeting]]
module = "./src/index.jsx"
target = "purchase.checkout.block.render"

[extensions.capabilities]
api_access = true
network_access = false
```

## Testing Extensions

```bash
shopify app dev  # starts tunnel and opens checkout preview
```

In the Shopify admin: Customize → Add block → Apps → your extension

## Notes

- Extensions run in a sandboxed iframe — no direct DOM access
- Use only the `@shopify/ui-extensions` APIs for rendering
- Network access from extensions requires explicit `network_access = true` capability
- Checkout extensions are versioned — deploy with `shopify app deploy`
