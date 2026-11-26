# The Astral Bureau — website infrastructure

Public site: https://astralbureau.com
Deployment: Cloudflare Workers Static Assets connected to GitHub, branch `main`.

## Layout
- `public/` — **the only directory deployed to the website**. Contains HTML, CSS and Workers asset headers.
- `wrangler.jsonc` — explicit Worker name and `assets.directory` configuration.
- `scripts/check_site.py` — validates required pages, internal links, noindex, and separation of public/private files.
- `.github/workflows/validate-site.yml` — runs checks on pull requests and main pushes.

## Workflow
1. Edit files inside `public/`, not the repository root.
2. Make a feature branch and open a pull request to `main`.
3. Wait for the GitHub validation action to pass; optionally check Cloudflare preview builds if enabled.
4. Merge into `main` to trigger the production deployment automatically.

Cloudflare dashboard production build settings:
- Build command: None
- Deploy command: `npx wrangler deploy`
- Root directory: `/`
- Production branch: `main`
- Cloudflare Worker name: `astral-bureau-site`

The dedicated asset directory prevents files like `README.md`, `.gitignore`, and Wrangler configuration from being uploaded as website content. `public/_headers` applies basic security headers and a temporary noindex header.

## Booking and privacy
This remains an **informational catalogue only**. Do not enable payments, appointment booking, or birth-data intake until a legitimate business contact address, finalized policies, secure data storage, retention rules, and payment providers are configured and reviewed.

Keep `noindex` in pages and security headers until the user expressly approves search indexing. Do not commit secrets, personal documents, or client birth records.

See Cloudflare Workers documentation:
- https://developers.cloudflare.com/workers/static-assets/
- https://developers.cloudflare.com/workers/static-assets/headers/
- https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/
