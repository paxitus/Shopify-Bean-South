# Accessibility Testing Guide for Shopify Themes

This guide provides step-by-step instructions for testing Shopify themes against WCAG 2.2 Level AA standards.

## Quick Testing Workflow

1. **Automated Testing** (10 minutes)
2. **Keyboard Navigation** (15 minutes)
3. **Screen Reader Testing** (20 minutes)
4. **Visual Testing** (10 minutes)
5. **Documentation** (5 minutes)

---

## 1. Automated Testing

### Using Chrome Lighthouse

1. Open your theme in Chrome (local or preview URL)
2. Open DevTools (F12)
3. Navigate to "Lighthouse" tab
4. Select "Accessibility" category
5. Click "Analyze page load"
6. **Target Score: 90+**

**Fix all issues flagged as:**
- Errors (red)
- Warnings (yellow)

### Using WAVE Browser Extension

1. Install [WAVE Extension](https://wave.webaim.org/extension/)
2. Navigate to each page type:
   - Home page
   - Collection page
   - Product page
   - Cart page
   - Blog page
   - Contact page
3. Click WAVE icon
4. **Target: 0 Errors, minimize Alerts**

**Focus on:**
- Missing alt text
- Empty links
- Missing form labels
- Contrast errors
- Missing landmarks

### Using axe DevTools

1. Install [axe DevTools](https://www.deque.com/axe/devtools/)
2. Open DevTools → axe DevTools tab
3. Click "Scan ALL of my page"
4. **Target: 0 Violations**

**Review:**
- Critical issues (must fix)
- Serious issues (should fix)
- Moderate issues (recommended)

### HTML Validation

1. Visit [W3C Validator](https://validator.w3.org/)
2. Enter your theme URL or upload HTML
3. Fix all errors
4. **Target: 0 Errors**

**Common Shopify Issues:**
- Duplicate IDs
- Unclosed tags
- Invalid attributes

---

## 2. Keyboard Navigation Testing

### Test All Pages Without Mouse

**Goal:** Navigate entire site using only keyboard

#### Basic Navigation Tests

| Action | Key | Expected Result | ✓ |
|--------|-----|-----------------|---|
| Tab forward | Tab | Focus moves to next interactive element | |
| Tab backward | Shift+Tab | Focus moves to previous element | |
| Activate link/button | Enter/Space | Element activates | |
| Close modal | Escape | Modal closes, focus returns | |
| Skip to content | Tab, Enter | Focus jumps to main content | |

#### Navigation Menu Tests

- [ ] Can open menu with keyboard
- [ ] Can navigate all menu items with Tab
- [ ] Can access dropdowns/mega menus with keyboard
- [ ] Can close menu with Escape
- [ ] Focus doesn't get trapped in menu
- [ ] Focus indicator always visible

#### Product Page Tests

- [ ] Can change product variants with keyboard
- [ ] Can increase/decrease quantity with keyboard
- [ ] Can add to cart with keyboard
- [ ] Can view product images with keyboard
- [ ] Can zoom images with keyboard
- [ ] All accordions keyboard accessible

#### Cart/Checkout Tests

- [ ] Can update quantities with keyboard
- [ ] Can remove items with keyboard
- [ ] Can apply discount codes with keyboard
- [ ] All form fields reachable with Tab
- [ ] Can submit forms with Enter

#### Filter/Search Tests

- [ ] Can open filters with keyboard
- [ ] Can select filter options with keyboard
- [ ] Can clear filters with keyboard
- [ ] Search is keyboard accessible
- [ ] Predictive search keyboard accessible

### Focus Visibility Test

**Check that focus is ALWAYS visible:**

```css
/* Test by adding this temporarily */
*:focus {
  outline: 5px solid red !important;
}
```

- [ ] Focus visible on all interactive elements
- [ ] Focus not hidden behind elements
- [ ] Focus has sufficient contrast (3:1 minimum)
- [ ] Custom focus styles work correctly

---

## 3. Screen Reader Testing

### Screen Readers by Platform

- **Windows:** NVDA (free) or JAWS
- **macOS:** VoiceOver (built-in)
- **iOS:** VoiceOver (built-in)
- **Android:** TalkBack (built-in)

### NVDA Testing (Windows)

**Start NVDA:**
1. Download and install [NVDA](https://www.nvaccess.org/)
2. Press Ctrl+Alt+N to start
3. Use Insert as NVDA key

**Essential Commands:**

| Action | Keys |
|--------|------|
| Read next item | Down Arrow |
| Read previous item | Up Arrow |
| Jump to next heading | H |
| Jump to next link | K |
| Jump to next landmark | D |
| Jump to next form field | F |
| List all headings | Insert+F7 |
| List all links | Insert+F7, Tab |
| Stop reading | Ctrl |

**Testing Checklist:**

- [ ] Page title announced when page loads
- [ ] Headings make sense out of context
- [ ] Can navigate by headings (H key)
- [ ] All images have appropriate alt text
- [ ] Forms have proper labels
- [ ] Required fields announced
- [ ] Error messages read clearly
- [ ] Buttons have clear labels
- [ ] Links describe their destination
- [ ] Modals/dialogs announced correctly
- [ ] Loading states announced
- [ ] Cart updates announced

### VoiceOver Testing (macOS)

**Start VoiceOver:**
- Press Cmd+F5 (or Cmd+Touch ID 3 times)

**Essential Commands:**

| Action | Keys |
|--------|------|
| Read next item | VO+Right Arrow |
| Read previous item | VO+Left Arrow |
| Interact with element | VO+Shift+Down Arrow |
| Stop interacting | VO+Shift+Up Arrow |
| Jump to next heading | VO+Cmd+H |
| Open rotor | VO+U |

**Test same checklist as NVDA above**

### Mobile Screen Reader Testing

#### iOS VoiceOver

1. Settings → Accessibility → VoiceOver → On
2. Or triple-click home/side button

**Gestures:**
- Swipe right: Next item
- Swipe left: Previous item
- Double tap: Activate
- Three-finger swipe: Scroll

#### Android TalkBack

1. Settings → Accessibility → TalkBack → On

**Gestures:**
- Swipe right: Next item
- Swipe left: Previous item
- Double tap: Activate
- Two-finger swipe: Scroll

### Common Issues to Listen For

- [ ] "Unlabeled button" or "Button"
- [ ] "Link" without destination
- [ ] "Image" without alt text
- [ ] Form fields without labels
- [ ] Tables read confusingly
- [ ] Unannounced state changes
- [ ] Content read in wrong order

---

## 4. Visual Testing

### Color Contrast Testing

**Using Chrome DevTools:**

1. Inspect element
2. Click color square in Styles panel
3. Check "Contrast ratio" section
4. Look for ✓ AA or ✗ AA

**Requirements:**
- Normal text: 4.5:1 or higher
- Large text (18pt+): 3:1 or higher
- UI components: 3:1 or higher

**Using WebAIM Contrast Checker:**

1. Visit [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
2. Enter foreground and background colors
3. Check WCAG AA results

**Test These Elements:**
- [ ] Body text
- [ ] Link text
- [ ] Button text
- [ ] Form labels
- [ ] Error messages
- [ ] Placeholder text
- [ ] Disabled elements

### Text Resize Testing

**Test at different zoom levels:**

1. Open theme
2. Zoom to 200% (Ctrl/Cmd + +)
3. Test functionality

**Checklist:**
- [ ] No horizontal scrolling at 200%
- [ ] All content still visible
- [ ] No overlapping text
- [ ] Buttons still usable
- [ ] Forms still functional
- [ ] Images don't cause overflow

### Mobile Testing

**Test on actual devices:**

- [ ] Touch targets at least 44×44 pixels
- [ ] Sufficient spacing between links
- [ ] No accidental activations
- [ ] Zoom works correctly
- [ ] No content hidden at mobile sizes

### Motion Testing

**Test with reduced motion:**

1. Enable reduced motion on your OS:
   - **Windows:** Settings → Ease of Access → Display → Show animations
   - **macOS:** System Preferences → Accessibility → Display → Reduce motion
   - **Chrome DevTools:** Cmd+Shift+P → "Emulate CSS prefers-reduced-motion"

2. Reload theme

**Checklist:**
- [ ] Animations significantly reduced or removed
- [ ] Parallax effects disabled
- [ ] Auto-playing carousels paused
- [ ] Transitions minimal
- [ ] No functionality lost

---

## 5. Page-Specific Testing

### Home Page

- [ ] Hero section accessible
- [ ] Featured products keyboard accessible
- [ ] Carousel controls keyboard accessible
- [ ] All links descriptive
- [ ] Announcement bar dismissible

### Collection/Product Listing

- [ ] Sort dropdown keyboard accessible
- [ ] Filters keyboard accessible
- [ ] Product cards keyboard accessible
- [ ] Pagination keyboard accessible
- [ ] Grid remains usable at 200% zoom

### Product Page

- [ ] Product images have alt text
- [ ] Image gallery keyboard accessible
- [ ] Variant selectors keyboard accessible
- [ ] Quantity controls keyboard accessible
- [ ] Add to Cart button labeled
- [ ] Reviews keyboard accessible
- [ ] Related products keyboard accessible

### Cart Page

- [ ] Quantity controls keyboard accessible
- [ ] Remove buttons labeled
- [ ] Discount code input labeled
- [ ] Subtotal/total clearly labeled
- [ ] Checkout button keyboard accessible
- [ ] Updates announced to screen readers

### Checkout

**Note:** Shopify handles checkout, but test:
- [ ] All form fields labeled
- [ ] Required fields marked
- [ ] Error messages clear
- [ ] Payment form accessible

### Search

- [ ] Search input labeled
- [ ] Search button labeled
- [ ] Predictive search keyboard accessible
- [ ] Results keyboard navigable
- [ ] No results message clear

### Blog

- [ ] Article headings structured properly
- [ ] Images have alt text
- [ ] Comments form accessible
- [ ] Category filters keyboard accessible
- [ ] Pagination keyboard accessible

---

## 6. Common Issues & Solutions

### Issue: "Skip to content" link missing

**Solution:**
```liquid
<a href="#MainContent" class="skip-to-content-link visually-hidden">
  Skip to content
</a>
```

### Issue: Images without alt text

**Solution:**
```liquid
{{ image | image_url: width: 800 | image_tag: alt: image.alt }}
```

### Issue: Form inputs without labels

**Solution:**
```liquid
<label for="email">Email address</label>
<input type="email" id="email" name="contact[email]">
```

### Issue: Buttons without labels

**Solution:**
```liquid
<button type="button" aria-label="Close menu">
  <span class="icon-close" aria-hidden="true"></span>
</button>
```

### Issue: Insufficient color contrast

**Solution:** Adjust colors in theme settings or CSS

### Issue: Focus not visible

**Solution:**
```css
*:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

---

## 7. Testing Schedule

### During Development
- Run automated tests after each significant change
- Test keyboard navigation for new features
- Verify color contrast for new colors

### Before Each Commit
- Quick Lighthouse scan
- Keyboard navigation test
- Visual check

### Before Going Live
- Full automated test suite
- Complete keyboard navigation test
- Screen reader test (at least one)
- Mobile device testing
- Contrast check all colors

### Monthly Maintenance
- Full accessibility audit
- Test with latest screen reader versions
- Update documentation

---

## 8. Documentation Template

After testing, document results:

```markdown
# Accessibility Test Results

**Date:** YYYY-MM-DD
**Tester:** Name
**Theme Version:** X.X.X
**Pages Tested:** Home, Collection, Product, Cart

## Automated Testing
- Lighthouse Score: XX/100
- WAVE Errors: X
- axe Violations: X

## Manual Testing
- Keyboard Navigation: Pass/Fail
- Screen Reader: Pass/Fail
- Color Contrast: Pass/Fail
- Text Resize: Pass/Fail

## Issues Found
1. Issue description
   - Severity: Critical/Serious/Moderate
   - Location: Page/component
   - Status: Open/Fixed

## Next Steps
- [ ] Fix critical issues
- [ ] Retest after fixes
- [ ] Update documentation
```

---

## 9. Tools Installation Guide

### Browser Extensions

**Chrome/Edge:**
- [WAVE](https://chrome.google.com/webstore/detail/wave-evaluation-tool/)
- [axe DevTools](https://chrome.google.com/webstore/detail/axe-devtools-web-accessibility/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) (built into Chrome DevTools)

**Firefox:**
- [WAVE](https://addons.mozilla.org/en-US/firefox/addon/wave-accessibility-tool/)
- [axe DevTools](https://addons.mozilla.org/en-US/firefox/addon/axe-devtools/)

### Screen Readers

**NVDA (Windows):**
```
1. Visit https://www.nvaccess.org/download/
2. Download latest version
3. Install and run
4. Press Ctrl+Alt+N to start
```

**VoiceOver (macOS):**
```
Built-in - no installation required
Press Cmd+F5 to start
```

---

## 10. Quick Reference

### Keyboard Shortcuts

| Action | Key |
|--------|-----|
| Tab forward | Tab |
| Tab backward | Shift+Tab |
| Activate | Enter or Space |
| Close modal | Escape |
| Scroll page | Arrow keys or Space |

### ARIA Attributes Quick Reference

```liquid
aria-label="descriptive text"
aria-labelledby="element-id"
aria-describedby="element-id"
aria-expanded="true/false"
aria-controls="element-id"
aria-hidden="true/false"
aria-live="polite/assertive"
aria-atomic="true/false"
role="button/navigation/main/etc"
```

### Minimum Requirements Summary

- ✅ All images have alt text
- ✅ All forms have labels
- ✅ Color contrast meets 4.5:1 (or 3:1 for large text)
- ✅ Keyboard navigation works everywhere
- ✅ Focus is always visible
- ✅ Skip links present
- ✅ Proper heading hierarchy
- ✅ Screen reader announcements work
- ✅ No keyboard traps
- ✅ Page titles unique and descriptive

---

**Remember:** Accessibility is an ongoing process, not a one-time fix. Test regularly and incorporate accessibility into your development workflow from the start.
