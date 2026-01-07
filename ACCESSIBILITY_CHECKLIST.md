# WCAG 2.2 Level AA Quick Checklist

Use this checklist during development and before deployment.

## Pre-Development Checklist

- [ ] Review ACCESSIBILITY.md guidelines
- [ ] Set up automated testing tools (Lighthouse, WAVE, axe)
- [ ] Install screen reader for testing (NVDA/VoiceOver)
- [ ] Bookmark contrast checker tool

---

## Development Checklist

### Every Component/Section

#### Images & Media
- [ ] All images have descriptive `alt` attributes
- [ ] Decorative images use `alt=""`
- [ ] Product images include product name in alt text
- [ ] Videos have captions (if applicable)
- [ ] Auto-playing media can be paused

#### Interactive Elements
- [ ] All buttons have descriptive labels
- [ ] Icon-only buttons have `aria-label`
- [ ] Links describe destination (no "click here")
- [ ] All interactive elements keyboard accessible
- [ ] Focus indicators visible (never `outline: none` without alternative)

#### Forms
- [ ] Every input has associated `<label>`
- [ ] Required fields marked clearly
- [ ] Error messages clear and specific
- [ ] Error messages associated with inputs (`aria-describedby`)
- [ ] Form validation doesn't rely on color alone

#### Structure
- [ ] Proper heading hierarchy (h1 → h2 → h3)
- [ ] One `<h1>` per page
- [ ] Semantic HTML (nav, main, article, aside, footer)
- [ ] Skip to content link present
- [ ] Page has unique `<title>`

#### Color & Contrast
- [ ] Text contrast minimum 4.5:1
- [ ] Large text contrast minimum 3:1
- [ ] UI components contrast minimum 3:1
- [ ] Information not conveyed by color alone
- [ ] Focus indicators have 3:1 contrast

#### Responsive & Zoom
- [ ] No horizontal scroll at 200% zoom
- [ ] Content readable at 200% zoom
- [ ] Touch targets minimum 44×44px
- [ ] Sufficient spacing between interactive elements

---

## Component-Specific Checklists

### Header/Navigation

- [ ] Skip to content link (first in tab order)
- [ ] Logo has alt text
- [ ] Main navigation has `role="navigation"`
- [ ] Menu toggle button labeled
- [ ] Mobile menu keyboard accessible
- [ ] Mobile menu closeable with Escape
- [ ] Dropdown menus keyboard accessible
- [ ] Current page indicated in navigation
- [ ] Search input labeled

### Hero/Banner

- [ ] Background images don't affect text readability
- [ ] Text contrast sufficient
- [ ] CTA buttons clearly labeled
- [ ] Image alt text descriptive (if hero uses img tag)

### Product Card

- [ ] Product image has alt with product name
- [ ] Product title is heading (h2 or h3)
- [ ] Price clearly labeled
- [ ] "Quick add" button descriptive
- [ ] "View product" link descriptive
- [ ] Variant selector keyboard accessible

### Product Page

- [ ] Product images have descriptive alt
- [ ] Image gallery keyboard accessible
- [ ] Image zoom keyboard accessible
- [ ] Variant options properly grouped (`<fieldset>`)
- [ ] Variant options have clear labels
- [ ] Color swatches have text labels
- [ ] Quantity controls keyboard accessible
- [ ] Add to cart button clearly labeled
- [ ] Out of stock clearly indicated
- [ ] Price changes announced to screen readers
- [ ] Product description has proper headings
- [ ] Reviews section keyboard accessible
- [ ] Accordion controls properly labeled

### Cart

- [ ] Cart items list semantic markup
- [ ] Quantity controls labeled
- [ ] Quantity controls keyboard accessible
- [ ] Remove buttons clearly labeled
- [ ] Empty cart message clear
- [ ] Subtotal/total clearly labeled
- [ ] Cart updates announced (`aria-live`)
- [ ] Discount code input labeled
- [ ] Checkout button keyboard accessible

### Filters & Search

- [ ] Filter button labeled
- [ ] Filter panel keyboard accessible
- [ ] Filter checkboxes/radios labeled
- [ ] Applied filters visible
- [ ] Clear filters button present
- [ ] Sort dropdown keyboard accessible
- [ ] Search input labeled
- [ ] Search button labeled
- [ ] Search results have headings
- [ ] No results message clear
- [ ] Predictive search keyboard accessible

### Modal/Dialog

- [ ] Uses `<dialog>` or proper ARIA
- [ ] `aria-modal="true"`
- [ ] Modal has accessible name
- [ ] Close button clearly labeled
- [ ] Closeable with Escape key
- [ ] Focus trapped within modal
- [ ] Focus returns after closing
- [ ] Background content inert

### Carousel/Slideshow

- [ ] Play/pause button present
- [ ] Play/pause button labeled
- [ ] Navigation buttons labeled
- [ ] Keyboard accessible
- [ ] Pagination keyboard accessible
- [ ] Auto-rotation can be stopped
- [ ] Current slide indicated

### Footer

- [ ] Footer has `role="contentinfo"` or `<footer>`
- [ ] Newsletter signup accessible
- [ ] Social media icons labeled
- [ ] Copyright information present
- [ ] Links organized logically

---

## Testing Checklist

### Automated Tests (5 minutes)

- [ ] Lighthouse accessibility score 90+
- [ ] WAVE extension: 0 errors
- [ ] axe DevTools: 0 violations
- [ ] HTML validator: 0 errors

### Keyboard Navigation (10 minutes)

- [ ] Tab through entire page
- [ ] All interactive elements reachable
- [ ] Focus always visible
- [ ] Logical tab order
- [ ] No keyboard traps
- [ ] Modals closeable with Escape
- [ ] Skip link works

### Screen Reader (15 minutes)

- [ ] Page title announced
- [ ] Headings navigable
- [ ] Images have alt text
- [ ] Forms labeled correctly
- [ ] Buttons labeled clearly
- [ ] Links describe destination
- [ ] Error messages read
- [ ] Dynamic updates announced

### Visual Tests (5 minutes)

- [ ] Zoom to 200% - no horizontal scroll
- [ ] Color contrast checked
- [ ] No information conveyed by color alone
- [ ] Text remains readable at 200%

### Mobile Tests (10 minutes)

- [ ] Touch targets adequate size
- [ ] Mobile menu accessible
- [ ] No accidental activations
- [ ] Gestures have alternatives
- [ ] VoiceOver/TalkBack test

---

## Page Type Checklists

### Home Page

- [ ] Hero accessible
- [ ] Featured collections accessible
- [ ] Featured products accessible
- [ ] Testimonials accessible
- [ ] Newsletter signup accessible
- [ ] All carousels accessible

### Collection Page

- [ ] Collection description readable
- [ ] Filter accessible
- [ ] Sort accessible
- [ ] Product grid accessible
- [ ] Pagination accessible
- [ ] Breadcrumbs present

### Product Page

- [ ] Product info accessible
- [ ] Variant selection accessible
- [ ] Add to cart accessible
- [ ] Image gallery accessible
- [ ] Reviews accessible
- [ ] Related products accessible

### Cart Page

- [ ] Cart items accessible
- [ ] Quantity controls accessible
- [ ] Remove items accessible
- [ ] Discount codes accessible
- [ ] Checkout button accessible

### Blog Page

- [ ] Article list accessible
- [ ] Article cards accessible
- [ ] Categories/tags accessible
- [ ] Search accessible
- [ ] Pagination accessible

### Article Page

- [ ] Article heading structure
- [ ] Images have alt text
- [ ] Comments form accessible
- [ ] Social share accessible
- [ ] Related articles accessible

### Contact Page

- [ ] Form fully accessible
- [ ] All fields labeled
- [ ] Required fields marked
- [ ] Error handling accessible
- [ ] Success message accessible

---

## Pre-Deployment Final Checklist

### Critical Items (Must Fix)

- [ ] All images have alt attributes
- [ ] All forms have labels
- [ ] All buttons have accessible names
- [ ] Skip to content link works
- [ ] Keyboard navigation functional
- [ ] Focus visible everywhere
- [ ] Color contrast meets minimums
- [ ] No automated test errors

### High Priority (Should Fix)

- [ ] Heading hierarchy correct
- [ ] Semantic HTML used
- [ ] ARIA used appropriately
- [ ] Page titles unique
- [ ] Language declared
- [ ] Screen reader tested
- [ ] Mobile tested

### Recommended (Nice to Have)

- [ ] 200% zoom tested
- [ ] Reduced motion respected
- [ ] Multiple browsers tested
- [ ] Multiple devices tested
- [ ] Documentation updated

---

## Issue Severity Guide

### 🔴 Critical (Block Deployment)
- Missing alt text on important images
- Forms without labels
- Keyboard traps
- Inaccessible checkout flow
- Color contrast below 3:1

### 🟠 Serious (Fix ASAP)
- Incorrect heading hierarchy
- Missing skip links
- Insufficient focus indicators
- Color contrast 3:1-4.4:1 (should be 4.5:1)
- Unlabeled icon buttons

### 🟡 Moderate (Fix Soon)
- Minor ARIA issues
- Inconsistent labeling
- Missing breadcrumbs
- Decorative images with alt text

### 🟢 Minor (Improve Over Time)
- Overly verbose alt text
- Redundant ARIA
- Non-critical HTML validation warnings

---

## Quick Fixes Reference

### Add Alt Text
```liquid
{{ image | image_url: width: 800 | image_tag: alt: "Description" }}
```

### Label Button
```liquid
<button type="button" aria-label="Close menu">×</button>
```

### Label Input
```liquid
<label for="email">Email</label>
<input type="email" id="email" name="email">
```

### Make Link Descriptive
```liquid
<a href="{{ product.url }}" aria-label="View {{ product.title }}">
  View details
</a>
```

### Add Skip Link
```liquid
<a href="#MainContent" class="skip-to-content-link">
  Skip to content
</a>
```

### Fix Focus Visibility
```css
*:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

### Announce Dynamic Changes
```liquid
<div role="status" aria-live="polite" aria-atomic="true">
  {{ notification_message }}
</div>
```

---

## Resources Quick Links

- [Full Guidelines](./ACCESSIBILITY.md)
- [Testing Guide](./ACCESSIBILITY_TESTING.md)
- [WCAG Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Shopify Accessibility Docs](https://shopify.dev/themes/best-practices/accessibility)

---

## Notes

- **Print this checklist** for quick reference during development
- **Review weekly** to stay familiar with requirements
- **Update** as you discover new patterns or issues
- **Share** with team members and collaborators

**Remember:** Accessibility is not optional. It's a legal requirement in many jurisdictions and the right thing to do for all users.

---

**Last Updated:** January 2026  
**WCAG Version:** 2.2 Level AA
