# Security

Key security practices for Shopify app and theme development.

## Webhook HMAC Validation

Always verify incoming webhooks — do not trust payload data without this check:

```python
import hmac
import hashlib
import base64

def verify_webhook(data: bytes, hmac_header: str, secret: str) -> bool:
    digest = hmac.new(
        secret.encode('utf-8'),
        data,
        digestmod=hashlib.sha256
    ).digest()
    computed = base64.b64encode(digest).decode('utf-8')
    return hmac.compare_digest(computed, hmac_header)
```

```javascript
const crypto = require('crypto');

function verifyWebhook(rawBody, hmacHeader, secret) {
  const hash = crypto
    .createHmac('sha256', secret)
    .update(rawBody, 'utf8')
    .digest('base64');
  return crypto.timingSafeEqual(Buffer.from(hash), Buffer.from(hmacHeader));
}
```

## OAuth State Parameter

Prevent CSRF during OAuth install flow:

```javascript
// Generate on install start
const state = crypto.randomBytes(16).toString('hex');
session.oauthState = state;

// Verify on callback
if (req.query.state !== session.oauthState) {
  return res.status(403).send('State mismatch');
}
```

## Access Token Storage

- **Never** store access tokens in client-side code or Liquid templates
- Store encrypted in a database, not in plain environment variables committed to git
- Use Shopify's session token for embedded app authentication (App Bridge)

## Theme Security

**Never output unescaped user content:**

```liquid
{# Bad #}
{{ customer.note }}

{# Good #}
{{ customer.note | escape }}
{{ customer.note | strip_html }}
```

**Validate URL params before using in Liquid:**

```liquid
{%- assign sort = request.param('sort_by') -%}
{%- if sort == 'price-asc' or sort == 'price-desc' or sort == 'title-asc' -%}
  {# safe to use #}
{%- endif -%}
```

## Content Security Policy

Shopify injects a CSP header — do not load external scripts that aren't allowlisted. Use `{{ content_for_header }}` correctly and avoid inline `onclick` handlers.

## API Key Exposure

- Never put `SHOPIFY_API_SECRET` in client-side JavaScript
- Never commit `.env` files with real credentials
- Rotate tokens immediately if exposed
- Use scoped access — only request the minimum scopes needed

## Checkout Extension Security

- Extensions run in a sandboxed iframe — no direct DOM access to checkout
- Use `useApplyAttributeChange` / `useApplyMetafieldChange` for data mutations
- Never send customer PII to third-party endpoints from an extension without explicit consent
