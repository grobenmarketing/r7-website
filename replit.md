# R7 Creative Marketing Website

## Overview
This is a static HTML website for R7 Creative, a marketing agency specializing in "4-Minute Marketing" for local businesses. The website showcases their "You Capture, We Create" service model.

## Project Structure
- `index.html` - Homepage with hero section and 4-minute decision system explanation
- `about.html` - Company story, philosophy, team, and location
- `how-it-works.html` - Detailed process explanation and service components
- `pricing.html` - Pricing information and service packages with expandable features
- `results.html` - Case studies and client results
- `media.html` - Media resources and social links
- `contact.html` - Contact information and inquiry form
- `styles.css` - Unified external stylesheet (~1517 lines) with CSS variables, components, and utilities
- `server.py` - Python HTTP server with cache control disabled
- `img/` - Folder for images (with README.md documentation)

## Technology Stack
- Pure HTML/CSS (no framework)
- Python 3.11 for serving static files
- Responsive design with mobile-first approach
- Google Fonts (Inter typeface)

## Design System
The website uses a retro-inspired 1960s color palette with CSS variables:
- **Deep Black**: #1a1a1a (--color-deep-black)
- **Freedom White**: #ffffff (--color-white)
- **Vintage Cream**: #e8e5d4 (--color-vintage-cream)
- **Space Age Teal**: #2a4a5c (--color-space-teal)
- **Atomic Orange**: #f7931e (--color-atomic-orange)
- **Launch Button Red**: #cf071d (--color-launch-red)
- **Brushed Metal**: #bdc3c7 (--color-brushed-metal)

## CSS Architecture
The `styles.css` file is organized into sections:
1. **CSS Variables** - Colors, typography, spacing, transitions
2. **Base & Reset** - Foundational styles
3. **Typography** - Headings, paragraphs, links
4. **Navigation** - Responsive nav with mobile menu
5. **Layout** - Container, sections, grids
6. **Components** - Cards, buttons, CTAs, pricing cards, team cards, etc.
7. **Utility Classes** - Text sizes/colors, spacing, backgrounds, borders, flexbox, etc.
8. **Animations** - Fade-in effects with delays
9. **Responsive Design** - Tablet and mobile breakpoints

### Key CSS Features
- **Zero inline styles** - All styling uses external CSS classes
- **CSS Variables** - Easy theme customization
- **Utility-first approach** - Reusable utility classes (.text-gradient, .max-w-800, .bg-cream, etc.)
- **Component classes** - Semantic components (.hero, .card, .pricing-card, .team-card, etc.)
- **Mobile-responsive** - Hamburger menu, responsive grids, optimized typography

## Navigation
- Consistent navigation across all 7 pages
- Active page highlighting (orange color)
- Mobile-responsive hamburger menu with JavaScript toggle
- JavaScript `toggleMenu()` function in each page for mobile menu functionality

## Running Locally
The server runs on port 5000 and serves files with cache control disabled to ensure updates are visible immediately.

```bash
python3 server.py
```

## Recent Changes
- 2025-10-23: Complete CSS refactoring completed
  - Consolidated all inline CSS into unified external stylesheet (styles.css)
  - Added 500+ lines of comprehensive utility classes
  - Removed ~197 inline style instances across HTML pages
  - Moved all page-specific <style> blocks to main stylesheet
  - All 7 pages now use CSS classes only (zero inline styles)
  - Preserved retro 1960s design aesthetic throughout
  - Navigation component added to all pages with mobile support
  - Created img/ folder with documentation for future image integration
  - Verified all pages with screenshots - no visual regressions

## Deployment Notes
- Deployment configured for autoscale (stateless static website)
- No build process needed
- Server binds to 0.0.0.0:5000 for Replit compatibility

## Future Enhancements
- User will add images to img/ folder
- Images will be integrated into HTML pages
- Navigation logo image will be added by user
