# The Astral Bureau — website

Source repository for `astralbureau.com`.

This is a deliberately minimal holding page, **not** a production booking/payments website. It mirrors the static HTML/CSS-in-repo approach used by `f-ritz/wolfram-site`, without copying Wolfram Chemical content.

## Files
- `index.html` — temporary landing page
- `style.css` — temporary visual design
- `_headers` — basic HTTP response headers for Cloudflare Pages
- `.gitignore` — avoid accidentally checking local artifacts and secrets into Git

## Cloudflare Pages setup
1. Cloudflare dashboard → **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**.
2. Authorize GitHub if necessary. If access is restricted to selected repositories, grant access to `f-ritz/astral-bureau-site`.
3. Select the repo and use:
   - Project name: `astral-bureau`
   - Production branch: `main`
   - Framework preset: `None`
   - Build command: `exit 0` (or blank for no build step)
   - Build output directory: `.` (repository root)
   - Root directory (advanced): repository root / default
4. **Save and Deploy**. Verify your temporary `*.pages.dev` URL.
5. In the Pages project → **Custom domains** → **Set up a domain** → add `astralbureau.com` (and optionally `www.astralbureau.com`). Because the domain is on Cloudflare, the dashboard should guide you through DNS creation.
6. Verify that a new commit on `main` triggers a production deployment. Other branches may create previews.

## Before public launch
- Replace temporary landing page with final website, policies, and booking/payment system.
- **Remove `noindex, nofollow`** in `index.html` when the real website is ready for search indexing.
- Do not commit secrets, customer birth details, other customer data, or payment credentials to this repo.
- This repo does not create a Cloudflare Pages project by itself. The Git integration is enabled from the Cloudflare dashboard.
