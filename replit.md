# R7 Creative Marketing Website

## Overview
This is a static HTML website for R7 Creative, a marketing agency specializing in "4-Minute Marketing" for local businesses. The website showcases their "You Capture, We Create" service model.

## Project Structure
- `index.html` - Homepage with hero section and 4-minute decision system explanation
- `about.html` - Company story, philosophy, team, and location
- `how-it-works.html` - Detailed process explanation and service components
- `pricing.html` - Pricing information and service packages
- `results.html` - Case studies and client results
- `media.html` - Media resources and social links
- `contact.html` - Contact information and inquiry form
- `server.py` - Python HTTP server with cache control disabled

## Technology Stack
- Pure HTML/CSS (no framework)
- Python 3.11 for serving static files
- Responsive design with mobile-first approach

## Design System
The website uses a retro-inspired color palette:
- **Deep Black**: #1a1a1a
- **Freedom White**: #ffffff
- **Vintage Cream**: #e8e5d4
- **Space Age Teal**: #2a4a5c
- **Atomic Orange**: #f7931e
- **Launch Button Red**: #cf071d
- **Brushed Metal**: #bdc3c7

## Running Locally
The server runs on port 5000 and serves files with cache control disabled to ensure updates are visible immediately.

```bash
python3 server.py
```

## Recent Changes
- 2025-10-23: Initial project setup in Replit environment
- Added Python HTTP server with no-cache headers
- Configured workflow for development server

## Deployment Notes
- Deployment configured for autoscale (stateless static website)
- No build process needed
- Server binds to 0.0.0.0:5000 for Replit compatibility
