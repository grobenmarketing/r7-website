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
The website features a professional 3-column navigation layout:
- **Logo Column (Left)**: R7 Creative logo image (135px width)
- **Menu Column (Center)**: Horizontal navigation links with dropdown menu
  - "How It Works" includes dropdown submenu to "Results" page
  - Active page highlighting in red color (#dc2626)
- **CTA Column (Right)**: Red "Get Started" button linking to Contact page
  - Button styling: red background (#dc2626), white text, rounded corners, hover effects
- **Mobile Responsive**: Hamburger menu toggle slides in nav-column from left
  - Dropdown submenu auto-expands on mobile (no hover needed)
  - CTA button hidden on mobile (accessible via Contact link)
- Consistent navigation structure across all 7 pages
- JavaScript `toggleMenu()` function toggles nav-column visibility on mobile

## Running Locally
The server runs on port 5000 and serves files with cache control disabled to ensure updates are visible immediately.

```bash
python3 server.py
```

## Recent Changes
- 2025-10-23: Navigation redesign completed
  - Implemented 3-column navigation layout (logo | menu | CTA)
  - Integrated R7 Creative logo image (r7creative-logo.png) into navigation
  - Added "How It Works" dropdown menu with "Results" submenu
  - Created red "Get Started" CTA button linking to Contact page
  - Updated navigation CSS with dropdown hover states and CTA styling
  - Updated navigation HTML across all 7 pages for consistency
  - Enhanced mobile responsive CSS for new nav structure
  - Updated toggleMenu() JavaScript to toggle nav-column wrapper
  - Active page highlighting now uses red color (#dc2626) matching CTA
  - Verified desktop and mobile navigation behavior with screenshots

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
- User will add additional images to img/ folder
- Images will be integrated into HTML pages as needed
