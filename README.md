# DefenseTechAZ

An independent directory of Arizona defense and dual-use technology companies.

## Edit the directory

**[data/companies.csv](data/companies.csv) is the source of truth.** Open it on GitHub, click the pencil, edit or add a row, and commit to `main` (or submit a pull request). Once GitHub Pages is enabled, each commit automatically validates the data, rebuilds the website, and deploys it. The Google Sheet is the initial import, not a live dependency.

Columns: `Company`, `City`, `Website`, `Blurb`, `Source`. All fields are required. Use full HTTPS website links, quote fields containing commas, keep company names unique, and include public sources for new listings. Avoid unsubstantiated claims about military customers or contracts. The CSV is available for download on the website, including its source links.

The initial 14 companies were imported from the owner's [Google Sheet](https://docs.google.com/spreadsheets/d/1qLFFtqne1_MPuG09vrafc4MYpN3rL478IO1mXH5B52s/edit), with Cryo X Co subsequently added. All 15 blurbs were reviewed against company-published sources on 2026-11-03; supporting URLs are recorded in each row's `Source` field. This checks alignment with public product descriptions, not independent testing of advertised performance. Locations remain from the seed except Cryo X Co (Tempe, company overview) and Corvus Industries (corrected to Tempe, company homepage).

The review removed the unsupported Crow vehicle-weight claim; replaced Fast DMS's marketplace description with its current manufacturing and coordination services; clarified that Smart Surface Robotics' robotics are in development; and described SpektreWorks' FLM136 as a threat-emulation aircraft rather than conflating it with a loitering munition. Hydronalix now reflects its current maritime mission portfolio without the unsupported SCARAB swarm description. Founder information is not part of this directory.

## GitHub Pages hosting

Website: **https://DrewSBAI.github.io/DefenseTechAZ/**

1. Ensure the account supports Pages for this repository (see below).
2. In the repository's **Settings → Pages**, set **Source** to **GitHub Actions**.
3. Under **Settings → Secrets and variables → Actions → Variables**, create a repository variable named `PAGES_ENABLED` with value `true`. This keeps deployments disabled until hosting is available, while build validation continues.
4. Run **Build and deploy directory** from the Actions tab, or push a change to `main`.
5. Wait for the deployment job to succeed. Subsequent edits publish automatically.

GitHub Pages from a private personal repository requires GitHub Pro. The standard Pages site is public even when its source repository is private. On GitHub Free, either upgrade to Pro or deliberately make the repository public when ready, then enable Pages. Do not change repository visibility merely to fix a deployment failure.

GitHub's documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages

This public repository belongs to the personal account **DrewSBAI**, not the Swarmbotics AI organization. The site links to GitHub for suggestions; anyone with a GitHub account can suggest an issue or pull request.

## Local preview

Requires Python 3. No packages or JavaScript build tools are needed.

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory _site
```

Open http://localhost:8000. Re-run the build after editing data or source files.

## Structure

- `data/companies.csv` — editable company records
- `site/` — HTML template, styling, and progressive search/filter controls
- `scripts/build.py` — validates CSV and generates escaped HTML in `_site/`
- `.github/workflows/pages.yml` — validates pull requests; builds and deploys `main`

The directory works without JavaScript; JavaScript adds search and location filtering. Generated files are not committed. GitHub Pages serves only the generated website and downloadable company CSV.
