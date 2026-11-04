# DefenseTechAZ

An independent directory of Arizona defense and dual-use technology companies.

**[Explore the directory →](https://drewsbai.github.io/DefenseTechAZ/)**

Find companies by name, capability, or location, and download the full list as CSV.

## Contribute

Know a company we should include, or see something that needs updating? [Open an issue](https://github.com/DrewSBAI/DefenseTechAZ/issues/new) or submit a pull request editing [data/companies.csv](data/companies.csv).

Each entry includes a company name, Arizona location, website, short description, and supporting source links. Keep descriptions factual and concise, cite company or other primary sources, and distinguish available products from technology in development.

Listings are informational and do not imply endorsement.

## Development

The site uses HTML, CSS, JavaScript, and a Python build script. No dependencies are required beyond Python 3.

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory _site
```

Open http://localhost:8000. Edit company records in `data/companies.csv` and website files in `site/`, then rebuild to preview changes. GitHub Actions validates pull requests and publishes updates to GitHub Pages when changes merge into `main`.
