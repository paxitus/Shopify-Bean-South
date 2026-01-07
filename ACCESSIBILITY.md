# WCAG 2.2 Level AA Accessibility Guidelines for Shopify Themes

This document provides a comprehensive checklist and guidelines for ensuring Shopify themes meet WCAG 2.2 Level AA accessibility standards.

## Table of Contents

1. [Perceivable](#1-perceivable)
2. [Operable](#2-operable)
3. [Understandable](#3-understandable)
4. [Robust](#4-robust)
5. [Shopify-Specific Considerations](#shopify-specific-considerations)

---

## 1. Perceivable

Information and user interface components must be presentable to users in ways they can perceive.

### 1.1 Text Alternatives

#### ✅ Images (1.1.1 - Level A)
- [ ] All `<img>` tags have meaningful `alt` attributes
- [ ] Decorative images use `alt=""` (empty alt)
- [ ] Complex images (charts, diagrams) have extended descriptions
- [ ] Product images have descriptive alt text including product name
- [ ] Logo images have alt text with company name

**Shopify Liquid Example:**
```liquid
{%- if section.settings.image != blank -%}
  <img
    src="{{ section.settings.image | image_url: width: 800 }}"
    alt="{{ section.settings.image.alt | escape }}"
    width="{{ section.settings.image.width }}"
    height="{{ section.settings.image.height }}"
    loading="lazy"
  >
{%- endif -%}
```

#### ✅ Form Controls (1.1.1 - Level A)
- [ ] All form inputs have associated `<label>` elements
- [ ] Buttons have descriptive text or `aria-label`
- [ ] Icon-only buttons have `aria-label` or `title` attributes

### 1.2 Time-based Media

#### ✅ Audio and Video (1.2.1, 1.2.2, 1.2.3 - Level A/AA)
- [ ] Videos have captions
- [ ] Audio content has transcripts
- [ ] Auto-playing media can be paused/stopped
- [ ] Media controls are keyboard accessible

### 1.3 Adaptable

#### ✅ Semantic Structure (1.3.1 - Level A)
- [ ] Proper heading hierarchy (h1 → h2 → h3, no skipping levels)
- [ ] One `<h1>` per page (typically site title or page title)
- [ ] Lists use proper markup (`<ul>`, `<ol>`, `<li>`)
- [ ] Tables use `<th>`, `<thead>`, `<tbody>`, and `scope` attributes
- [ ] Forms use `<fieldset>` and `<legend>` for grouped inputs

**Shopify Heading Example:**
```liquid
{%- comment -%} Page title should be h1 {%- endcomment -%}
<h1 class="product__title">{{ product.title }}</h1>

{%- comment -%} Section headings should be h2 {%- endcomment -%}
<h2 class="section__heading">{{ section.settings.heading }}</h2>
```

#### ✅ Meaningful Sequence (1.3.2 - Level A)
- [ ] Content reading order makes sense when CSS is disabled
- [ ] Visual order matches DOM order
- [ ] Mobile navigation doesn't break logical flow

#### ✅ Sensory Characteristics (1.3.3 - Level A)
- [ ] Instructions don't rely solely on shape, size, or visual location
- [ ] Color is not the only means of conveying information

### 1.4 Distinguishable

#### ✅ Color Contrast (1.4.3 - Level AA)
- [ ] Normal text: minimum 4.5:1 contrast ratio
- [ ] Large text (18pt+/14pt+ bold): minimum 3:1 contrast ratio
- [ ] UI components and graphics: minimum 3:1 contrast ratio
- [ ] Link text distinguishable from surrounding text

**Tools for Testing:**
- Chrome DevTools Lighthouse
- WebAIM Contrast Checker
- WAVE Browser Extension

#### ✅ Resize Text (1.4.4 - Level AA)
- [ ] Text can be resized up to 200% without loss of functionality
- [ ] No horizontal scrolling at 200% zoom
- [ ] Use relative units (rem, em) instead of px for font sizes

#### ✅ Images of Text (1.4.5 - Level AA)
- [ ] Use actual text instead of images of text when possible
- [ ] Logo images are acceptable
- [ ] Essential images (graphs) are acceptable with alt text

#### ✅ Focus Visible (1.4.11 - Level AA, new in 2.2)
- [ ] Focus indicators are clearly visible
- [ ] Focus indicators have minimum 3:1 contrast
- [ ] Custom focus styles don't reduce visibility

**CSS Example:**
```css
/* Ensure visible focus indicators */
*:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

/* For links and buttons */
a:focus-visible,
button:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}
```

#### ✅ Text Spacing (1.4.12 - Level AA)
- [ ] Content adapts when users override text spacing
- [ ] No loss of functionality with increased spacing

#### ✅ Content on Hover/Focus (1.4.13 - Level AA)
- [ ] Hover/focus content is dismissible without moving pointer
- [ ] Content remains visible while hovering
- [ ] Content can be hovered over itself

---

## 2. Operable

User interface components and navigation must be operable.

### 2.1 Keyboard Accessible

#### ✅ Keyboard Navigation (2.1.1 - Level A)
- [ ] All interactive elements accessible via keyboard
- [ ] Tab order is logical and intuitive
- [ ] No keyboard traps (can navigate away from all elements)
- [ ] Custom dropdowns/modals are keyboard accessible

**Shopify Menu Drawer Example:**
```liquid
<button
  type="button"
  class="header__menu-toggle"
  aria-controls="menu-drawer"
  aria-expanded="false"
  aria-label="Open menu"
>
  <span class="icon-hamburger"></span>
</button>

<nav id="menu-drawer" aria-label="Main navigation" hidden>
  {%- comment -%} Menu content {%- endcomment -%}
</nav>
```

#### ✅ No Keyboard Trap (2.1.2 - Level A)
- [ ] Focus can move away from all components using only keyboard
- [ ] Modal dialogs can be closed with Escape key
- [ ] Mega menus can be exited with keyboard

#### ✅ Focus Order (2.4.3 - Level A)
- [ ] Focus order follows visual order
- [ ] Skip links appear first in tab order

### 2.2 Enough Time

#### ✅ Timing Adjustable (2.2.1 - Level A)
- [ ] No automatic timeouts for user actions
- [ ] Users can extend time limits if required
- [ ] Countdown timers (sales) have pause/extend options

### 2.3 Seizures and Physical Reactions

#### ✅ Three Flashes or Below (2.3.1 - Level A)
- [ ] No content flashes more than 3 times per second
- [ ] Animations can be paused or disabled

**CSS Example using prefers-reduced-motion:**
```css
/* Respect user's motion preferences */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 2.4 Navigable

#### ✅ Skip Links (2.4.1 - Level A)
- [ ] "Skip to content" link at the top of every page
- [ ] Skip link is visible on focus
- [ ] Skip link jumps to main content area

**Shopify Skip Link Example:**
```liquid
{%- comment -%} In layout/theme.liquid {%- endcomment -%}
<a href="#MainContent" class="skip-to-content-link visually-hidden">
  {{ 'accessibility.skip_to_text' | t }}
</a>

<main id="MainContent" role="main" tabindex="-1">
  {{ content_for_layout }}
</main>
```

**CSS for Skip Link:**
```css
.skip-to-content-link {
  position: absolute;
  left: -10000px;
  top: auto;
  width: 1px;
  height: 1px;
  overflow: hidden;
}

.skip-to-content-link:focus {
  position: fixed;
  top: 10px;
  left: 10px;
  width: auto;
  height: auto;
  padding: 1rem;
  background: white;
  border: 2px solid black;
  z-index: 10000;
}
```

#### ✅ Page Titles (2.4.2 - Level A)
- [ ] Every page has a unique, descriptive `<title>`
- [ ] Title format: "Page Name - Site Name"
- [ ] Product pages include product name in title

**Shopify Title Example:**
```liquid
{%- comment -%} In layout/theme.liquid {%- endcomment -%}
<title>
  {{ page_title }}
  {%- if current_tags %} &ndash; tagged "{{ current_tags | join: ', ' }}"{% endif -%}
  {%- if current_page != 1 %} &ndash; Page {{ current_page }}{% endif -%}
  {%- unless page_title contains shop.name %} &ndash; {{ shop.name }}{% endunless -%}
</title>
```

#### ✅ Focus Order (2.4.3 - Level A)
- [ ] Tabbing order is logical
- [ ] Hidden content not in tab order

#### ✅ Link Purpose (2.4.4 - Level A)
- [ ] Link text describes destination or purpose
- [ ] Avoid "click here" or "read more" without context
- [ ] Use `aria-label` to provide context if needed

**Shopify Link Example:**
```liquid
{%- comment -%} Bad: No context {%- endcomment -%}
<a href="{{ product.url }}">Read more</a>

{%- comment -%} Good: Descriptive text {%- endcomment -%}
<a href="{{ product.url }}">View {{ product.title }} details</a>

{%- comment -%} Good: Using aria-label for context {%- endcomment -%}
<a href="{{ product.url }}" aria-label="View details for {{ product.title }}">
  Read more
</a>
```

#### ✅ Multiple Ways (2.4.5 - Level AA)
- [ ] Multiple ways to find pages (menu, search, sitemap)
- [ ] Search functionality available
- [ ] Breadcrumb navigation for deep pages

#### ✅ Headings and Labels (2.4.6 - Level AA)
- [ ] Headings are descriptive
- [ ] Form labels clearly describe purpose
- [ ] Section headings help users understand content organization

#### ✅ Focus Visible (2.4.7 - Level AA)
- [ ] Keyboard focus is always visible
- [ ] Never use `outline: none` without providing alternative

### 2.5 Input Modalities

#### ✅ Pointer Gestures (2.5.1 - Level A)
- [ ] Multi-point gestures have single-point alternatives
- [ ] Pinch-to-zoom has zoom buttons

#### ✅ Pointer Cancellation (2.5.2 - Level A)
- [ ] Click events on mouse up, not mouse down
- [ ] Touch events on touch end, not touch start

#### ✅ Label in Name (2.5.3 - Level A)
- [ ] Visible label text is included in accessible name
- [ ] Button text matches aria-label (if used)

#### ✅ Target Size (2.5.5 - Level AAA, but recommended)
- [ ] Interactive elements at least 44×44 CSS pixels
- [ ] Mobile touch targets at least 48×48 pixels
- [ ] Sufficient spacing between interactive elements

**CSS Example:**
```css
/* Ensure minimum touch target size */
button,
a,
input[type="checkbox"],
input[type="radio"] {
  min-width: 44px;
  min-height: 44px;
}
```

---

## 3. Understandable

Information and operation of user interface must be understandable.

### 3.1 Readable

#### ✅ Language of Page (3.1.1 - Level A)
- [ ] `<html>` tag has `lang` attribute
- [ ] Language attribute matches primary language

**Shopify Example:**
```liquid
{%- comment -%} In layout/theme.liquid {%- endcomment -%}
<!DOCTYPE html>
<html lang="{{ request.locale.iso_code }}">
```

#### ✅ Language of Parts (3.1.2 - Level AA)
- [ ] Foreign language content has `lang` attribute
- [ ] Product descriptions in other languages marked up

### 3.2 Predictable

#### ✅ On Focus (3.2.1 - Level A)
- [ ] No automatic changes when element receives focus
- [ ] Forms don't auto-submit on focus

#### ✅ On Input (3.2.2 - Level A)
- [ ] Changing input doesn't automatically cause context change
- [ ] Dropdowns don't navigate on selection without submit

#### ✅ Consistent Navigation (3.2.3 - Level AA)
- [ ] Navigation appears in same location on every page
- [ ] Menu items in consistent order

#### ✅ Consistent Identification (3.2.4 - Level AA)
- [ ] Same functionality has same labels throughout
- [ ] Icons used consistently (cart icon always means cart)

### 3.3 Input Assistance

#### ✅ Error Identification (3.3.1 - Level A)
- [ ] Form errors clearly identified
- [ ] Error messages associated with inputs
- [ ] Required fields clearly marked

**Shopify Form Error Example:**
```liquid
{%- if form.errors -%}
  <div class="form__errors" role="alert">
    <h2 class="form__errors-heading">
      {{ 'templates.contact.form.error_heading' | t }}
    </h2>
    <ul>
      {%- for field in form.errors -%}
        <li>
          <a href="#{{ field }}">
            {{ form.errors.messages[field] }}
          </a>
        </li>
      {%- endfor -%}
    </ul>
  </div>
{%- endif -%}

<input
  type="email"
  id="email"
  name="contact[email]"
  aria-required="true"
  {% if form.errors contains 'email' %}
    aria-invalid="true"
    aria-describedby="email-error"
  {% endif %}
>
{% if form.errors contains 'email' %}
  <span id="email-error" class="form__error">
    {{ form.errors.messages['email'] }}
  </span>
{% endif %}
```

#### ✅ Labels or Instructions (3.3.2 - Level A)
- [ ] All form fields have labels
- [ ] Required fields marked with asterisk AND text
- [ ] Format requirements explained (e.g., "MM/DD/YYYY")

#### ✅ Error Suggestion (3.3.3 - Level AA)
- [ ] Error messages suggest corrections
- [ ] Helpful, specific error messages

#### ✅ Error Prevention (3.3.4 - Level AA)
- [ ] Confirmation required for financial/legal transactions
- [ ] Review page before final submission
- [ ] Ability to undo or correct data

---

## 4. Robust

Content must be robust enough to be interpreted by a wide variety of user agents, including assistive technologies.

### 4.1 Compatible

#### ✅ Valid HTML (4.1.1 - Level A)
- [ ] No duplicate IDs
- [ ] Properly nested elements
- [ ] Complete start and end tags
- [ ] Valid HTML5 syntax

**Test with:**
- W3C HTML Validator
- Chrome DevTools Console

#### ✅ Name, Role, Value (4.1.2 - Level A)
- [ ] All interactive elements have accessible names
- [ ] Custom controls have appropriate ARIA roles
- [ ] State changes communicated to assistive technologies

**ARIA Examples:**
```liquid
{%- comment -%} Accordion {%- endcomment -%}
<button
  type="button"
  aria-expanded="false"
  aria-controls="panel-{{ section.id }}"
>
  {{ section.settings.heading }}
</button>

<div id="panel-{{ section.id }}" hidden>
  {{ section.settings.content }}
</div>

{%- comment -%} Modal {%- endcomment -%}
<dialog
  id="modal-{{ section.id }}"
  aria-modal="true"
  aria-labelledby="modal-title-{{ section.id }}"
>
  <h2 id="modal-title-{{ section.id }}">{{ section.settings.modal_title }}</h2>
  <!-- Modal content -->
</dialog>
```

#### ✅ Status Messages (4.1.3 - Level AA, new in 2.1)
- [ ] Dynamic status messages use appropriate ARIA live regions
- [ ] Loading states announced to screen readers
- [ ] Success/error messages use `role="status"` or `role="alert"`

**Shopify Cart Example:**
```liquid
<div
  id="cart-notification"
  role="status"
  aria-live="polite"
  aria-atomic="true"
  class="cart-notification"
>
  <p>{{ product.title }} added to cart</p>
</div>
```

---

## Shopify-Specific Considerations

### Product Pages

- [ ] Product images have descriptive alt text
- [ ] Variant selectors are keyboard accessible
- [ ] Color swatches have text labels (not just color)
- [ ] Size selectors clearly labeled
- [ ] "Add to Cart" button has clear label
- [ ] Out of stock clearly indicated
- [ ] Price changes announced to screen readers

**Variant Selector Example:**
```liquid
<fieldset class="variant-input">
  <legend class="variant-input__legend">
    {{ option.name }}
  </legend>
  {%- for value in option.values -%}
    <input
      type="radio"
      id="{{ section.id }}-{{ option.position }}-{{ forloop.index0 }}"
      name="{{ option.name }}"
      value="{{ value | escape }}"
      {% if option.selected_value == value %}checked{% endif %}
    >
    <label for="{{ section.id }}-{{ option.position }}-{{ forloop.index0 }}">
      {{ value }}
    </label>
  {%- endfor -%}
</fieldset>
```

### Navigation

- [ ] Mega menus keyboard accessible
- [ ] Mobile menu doesn't trap focus
- [ ] Menu drawer can be closed with Escape
- [ ] Breadcrumbs use proper markup

### Search

- [ ] Search button has label
- [ ] Search input has label
- [ ] Predictive search results keyboard accessible
- [ ] Search results have clear headings

### Cart and Checkout

- [ ] Cart quantity controls keyboard accessible
- [ ] Remove item buttons clearly labeled
- [ ] Cart total updates announced
- [ ] Checkout form fields properly labeled
- [ ] Payment errors clearly communicated

### Filters and Sorting

- [ ] Filter options keyboard accessible
- [ ] Applied filters clearly indicated
- [ ] "Clear all" option available
- [ ] Sort dropdown keyboard accessible
- [ ] Filter changes update content accessibly

---

## Testing Checklist

### Automated Testing
- [ ] Lighthouse accessibility audit (score 90+)
- [ ] WAVE browser extension (0 errors)
- [ ] axe DevTools (0 violations)
- [ ] HTML validator (0 errors)

### Manual Testing
- [ ] Keyboard-only navigation
- [ ] Screen reader testing (NVDA/JAWS/VoiceOver)
- [ ] 200% zoom test
- [ ] Color contrast check
- [ ] Mobile device testing

### Browser Testing
- [ ] Chrome + ChromeVox
- [ ] Firefox
- [ ] Safari + VoiceOver
- [ ] Edge

---

## Resources

### Official Documentation
- [WCAG 2.2 Guidelines](https://www.w3.org/WAI/WCAG22/quickref/)
- [Shopify Theme Accessibility](https://shopify.dev/themes/best-practices/accessibility)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)

### Testing Tools
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [WAVE](https://wave.webaim.org/extension/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

### Screen Readers
- [NVDA](https://www.nvaccess.org/) (Windows, free)
- [JAWS](https://www.freedomscientific.com/products/software/jaws/) (Windows)
- VoiceOver (macOS/iOS, built-in)
- TalkBack (Android, built-in)

---

## Maintenance

This document should be reviewed and updated:
- With each major theme update
- When WCAG guidelines are updated
- When new Shopify features are added
- Based on user feedback and testing results

**Last Updated:** January 2026  
**WCAG Version:** 2.2 Level AA  
**Shopify Theme Version:** Compatible with Online Store 2.0
