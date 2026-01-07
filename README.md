# Bean South Coffee - Shopify Theme

This repository contains the Shopify theme for [Bean South Coffee](https://bean-south-coffee-2.myshopify.com/), built on the Lowthian-Crave theme.

## Project Goals

- Maintain WCAG 2.2 Level AA accessibility standards
- Provide a modern, user-friendly shopping experience
- Support Bean South Coffee's brand and product offerings

## Local Development Setup

### Prerequisites

- Node.js 20+ (managed via nvm)
- Shopify CLI
- Git with SSH authentication to GitHub

### Getting Started

1. **Clone the repository:**
```bash
git clone git@github.com:paxitus/Shopify-Bean-South.git
cd Shopify-Bean-South
```

2. **Authenticate with Shopify:**
```bash
shopify auth login
```

3. **Start the development server:**
```bash
shopify theme dev --store bean-south-coffee-2.myshopify.com
```

The development server will start at `http://127.0.0.1:9292`

### Development Workflow

1. Make changes to theme files locally
2. Changes automatically sync to the preview URL
3. Refresh your browser to see updates
4. Commit changes to Git:
```bash
git add .
git commit -m "Description of changes"
git push
```

### Theme Structure

```
├── assets/          # CSS, JavaScript, images
├── config/          # Theme settings
├── layout/          # Theme layouts
├── locales/         # Translation files
├── sections/        # Reusable sections
├── snippets/        # Reusable code snippets
└── templates/       # Page templates
```

## Deployment

### Push to Live Theme
```bash
shopify theme push --store bean-south-coffee-2.myshopify.com
```

### Push to Specific Theme
```bash
shopify theme push --theme [THEME_ID] --store bean-south-coffee-2.myshopify.com
```

## Accessibility Compliance

This theme is maintained to meet WCAG 2.2 Level AA standards. All contributions should:
- Ensure proper semantic HTML
- Maintain keyboard navigation support
- Provide appropriate ARIA labels
- Maintain sufficient color contrast ratios
- Include alt text for images

## Resources

- [Shopify Theme Documentation](https://shopify.dev/docs/themes)
- [Liquid Reference](https://shopify.dev/docs/api/liquid)
- [WCAG 2.2 Guidelines](https://www.w3.org/WAI/WCAG22/quickref/)

## License

Proprietary - Bean South Coffee
