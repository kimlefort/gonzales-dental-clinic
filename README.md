# Gonzales Dental — design proposal

Active design: `templates/clinic/campaign.html`, its reusable `partials/`, `static/clinic/campaign.css`, and `static/clinic/campaign.js`. Published business content is in `clinic/content.py`; source attribution and preview limitations are in `CONTENT_SOURCES.md`.

Second edition includes internal About, History, FAQs, ten treatment pages and four shareable branch pages. Branch selection updates Google maps, contacts, Facebook destinations and explicitly dated review-rating snapshots. The new campaign portrait and Obrero interior are real published assets. Other branches link to their own Facebook photography until approved interior images are available.

## Start locally

1. Create and activate a Python virtual environment.
2. Run `pip install -r requirements.txt`.
3. Run `python manage.py migrate`.
4. Run `python manage.py test clinic` to check rendering, branch contacts, and the disabled prototype booking endpoint.
5. Run `python manage.py runserver` and open `http://127.0.0.1:8000/`.

If port 8000 is already serving an older copy, run `python manage.py runserver 8001` and open `http://127.0.0.1:8001/` instead. Open the project folder containing `manage.py` in VS Code; use Terminal → New Terminal for these commands. Do not open the Django HTML files directly or with Live Server.

## URLs to try

- `/about/` and `/about/history/`
- `/services/` and `/services/cosmetic-dentistry/`
- `/faqs/`
- `/clinics/obrero/`, `/clinics/matina/`, `/clinics/gensan/`, `/clinics/digos/`
- `/?branch=digos#appointment` selects Digos on the homepage.

Explicit branch-page URLs take precedence over saved browser preferences. Maps require internet access; direct Google and Facebook links provide fallbacks. Facebook timelines and live review APIs are not integrated. No React or Node build step is required.

## Before publishing

The site uses published Facebook branch contact records and WordPress service/history information. Opening hours are not guessed. Booking actions connect to the selected clinic directly; no booking form submits to a clinic system.

For a public launch, confirm content and photo usage with the clinic, use original high-resolution assets, upgrade the Python 3.9 / Django 4.2 preview runtime, configure production settings, and remove the concept label and noindex only after approval. This project has not been deployed.
