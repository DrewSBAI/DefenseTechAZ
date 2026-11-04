"""Validate the canonical CSV and build a dependency-free GitHub Pages site."""
import csv
import html
import shutil
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def build():
    with (ROOT / 'data/companies.csv').open(newline='', encoding='utf-8') as source:
        reader = csv.DictReader(source)
        required = {'Company', 'City', 'Website', 'Blurb', 'Source'}
        if set(reader.fieldnames or []) != required:
            raise ValueError('CSV columns must be: ' + ', '.join(sorted(required)))
        companies = list(reader)
    if not companies:
        raise ValueError('The directory must contain at least one company.')
    names = set()
    for company in companies:
        if None in company or any(value is None for value in company.values()):
            raise ValueError('Malformed CSV row')
        if any(not company[field].strip() for field in required):
            raise ValueError('Missing required field: ' + repr(company))
        url = urlsplit(company['Website'])
        if url.scheme not in {'https', 'http'} or not url.netloc:
            raise ValueError('Invalid company website: ' + company['Website'])
        key = company['Company'].strip().casefold()
        if key in names:
            raise ValueError('Duplicate company: ' + company['Company'])
        names.add(key)
    companies.sort(key=lambda c: c['Company'].casefold())
    rows = []
    for index, company in enumerate(companies, 1):
        c = {key: html.escape(value, quote=True) for key, value in company.items()}
        rows.append(f'''<tr data-city="{c['City']}">
          <td class="number">{index:02d}</td>
          <th scope="row"><a href="{c['Website']}">{c['Company']} <span aria-hidden="true">↗</span></a></th>
          <td class="city">{c['City']}</td><td class="description">{c['Blurb']}</td>
        </tr>''')
    cities = sorted({c['City'] for c in companies})
    options = ''.join(f'<option>{html.escape(city)}</option>' for city in cities)
    template = (ROOT / 'site/index.html').read_text(encoding='utf-8')
    for token, value in {'{{ROWS}}': '\n'.join(rows), '{{COUNT}}': str(len(companies)), '{{CITIES}}': options}.items():
        template = template.replace(token, value)
    output = ROOT / '_site'
    output.mkdir(exist_ok=True)
    (output / 'index.html').write_text(template, encoding='utf-8')
    for filename in ('style.css', 'app.js'):
        shutil.copyfile(ROOT / 'site' / filename, output / filename)
    shutil.copyfile(ROOT / 'data/companies.csv', output / 'companies.csv')
    (output / '.nojekyll').touch()
    print(f'Built {len(companies)} companies into {output}')


if __name__ == '__main__':
    build()
