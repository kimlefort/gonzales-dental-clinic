# Content and image provenance

Updated 14 September 2026. This is a local design proposal, not a published official site.

## Editorial rules

- Use published business facts, not invented ratings, patient counts, treatment guarantees, prices or opening hours.
- Editorial headings such as “A shared calling” are design copy, not quotations or clinical claims.
- Current Facebook branch contact records take priority over the older single-branch WordPress footer. Matina is the current branch; Mintal appears in historical WordPress text, not the current branch list.
- Services represent the WordPress group's published menu, not independently confirmed availability at every branch. The site asks visitors to confirm with their chosen clinic.

## Written sources

- https://gonzalesdentalclinic.wordpress.com/ — exact tagline, “Three Generations of Dental Care”.
- https://gonzalesdentalclinic.wordpress.com/services/ — listed treatments, materials, braces and denture options. Individual service pages were read in the browser on 14 September; concise paraphrases now appear on ten internal treatment pages. Their exact source URLs are stored in `clinic/content.py`. Newly restored options include the published cosmetic treatments, frenectomy/frenuloplasty and metal-framework dentures. Unqualified painlessness, guaranteed longevity, historical success claims and prescriptive medical advice were not copied.
- https://gonzalesdentalclinic.wordpress.com/our-history/ — founded in 1960 by Dr. Cornelia “Nelly” Gonzales; Dean joined around 1975; Alyssa continued the family practice.
- https://gonzalesdentalclinic.wordpress.com/meet-our-team/ — Dean's university, Alyssa's university and 2019 licensure result. Old staff ages and claims of current academic appointments deliberately not repeated.
- https://www.facebook.com/gonzales.dentalclinic — Obrero address, phone, email.
- https://www.facebook.com/profile.php?id=61559646209197 — Matina address, phone, email.
- https://www.facebook.com/profile.php?id=61574243505145 — Gensan address, phone, email.
- https://www.facebook.com/profile.php?id=61579192551478 — Digos address, phone, email.

## Image sources

- `static/clinic/images/campaign-original.png`: user-provided original banner screenshot, copied without changing pixels. Hero is a CSS crop, not AI-generated or reconstructed. Exact slogan and family-care line are taken from this banner. Image is limited to screenshot resolution.
- `static/clinic/images/logo-original.png`: user-provided logo, copied without changing pixels. CSS crop conceals the Obrero-specific line in the shared header; CSS colour filter gives it a gold tone.
- `static/clinic/images/nelly.jpg`: https://gonzalesdentalclinic.wordpress.com/wp-content/uploads/2021/08/241106749_851722732400476_6393129954494190725_n-3.jpg?w=901
- `static/clinic/images/dean.jpg`: https://gonzalesdentalclinic.wordpress.com/wp-content/uploads/2021/08/76259_461601004653_983157_n.jpg?w=366
- `static/clinic/images/alyssa-ceremony.jpg`: https://gonzalesdentalclinic.wordpress.com/wp-content/uploads/2021/08/67372651_2329697520617384_8116837781067530240_n-2.jpg?w=1024
- `alyssa.jpg` is an unused downloaded clinical photograph. It does not appear on the website.

Photos were visually checked against the source page. Original full-resolution images and permission for public website use should be obtained from the clinic if the proposal is accepted.

## Booking and privacy

The website does not submit appointment requests. Buttons open a phone call, the branch's Facebook page, or email. No messages were sent during development. A branch preference is stored locally in the browser. Existing prototype appointment models/data are preserved, but the former unvalidated POST endpoint is disabled.

## Preview limits

Noindex metadata and a footer identify the design as a concept. No site was deployed. Fonts are loaded from Google Fonts with local fallbacks. Django 4.2 is used by the existing Python 3.9 environment for this local preview; upgrade Python and Django to a supported release before public deployment. The old `home.html`, `site.css`, and `site.js` are retained as unused first-draft assets; the active design is `campaign.html`, `campaign.css`, and `campaign.js`.

## Second edition: content, maps and photographs

- About: https://gonzalesdentalclinic.wordpress.com/about-us-2/ — read directly in the browser; introduction adapted rather than copied verbatim.
- First visit: https://gonzalesdentalclinic.wordpress.com/your-first-visit-2/ — arrival recommendation, forms and broad visit sequence. Old COVID-era instructions are not presented as current requirements.
- Payment: https://gonzalesdentalclinic.wordpress.com/modes-of-payment/ — page loaded in the browser but only a title was published; no accepted payment methods asserted.
- Consultation: https://gonzalesdentalclinic.wordpress.com/services/consultation-and-diagnostics/ — medical history, case-dependent diagnostics, permission for photographs and patient privacy. New website does not collect medical details.
- Active hero `campaign-portrait.jpg`: https://www.facebook.com/photo/?fbid=1499705248841603&set=pcb.1499705325508262 — downloaded original displayed asset, 3072 × 3840 pixels, JPEG. Original pixels preserved; responsive crop is CSS only. This is the cream-outfit portrait in the user-provided campaign post, not generated imagery. The former banner asset is retained but unused.
- Active header logo: the two original logo components are repositioned using separate CSS crops; no AI-generated replacement or raster edit. The old page is preserved as `campaign-v1.html`, unused.
- `obrero-lobby.webp`: clinic-owner-attributed photo on the Obrero Google listing, 1207 × 679. Inspected in the gallery (owner credit “Gonzales Dental Group - Obrero”, displayed age “a month ago”). Google photo identity: `CAoSHENJQUJJaEJkSHYyTmxfRm9iUmxLcUZLY0hQUk4`. Original asset downloaded unchanged. Shown only as Obrero, never assigned to the other branches. Local cached asset is for private proposal review; confirm licensing and obtain owner originals for a public launch.

### Branch map records

All four user-supplied links were resolved in the browser, and business names and phone numbers matched the existing branch records. CID identifiers below identify the exact listings, not approximate address searches.

| Branch | User source | Google CID | Observed rating / count |
| --- | --- | --- | --- |
| Obrero | https://share.google/JKBg5rr2LafxHpK3H | 3342764382200778387 | 4.6 / 22 |
| Matina | https://share.google/wzJvZWlu6QbRTa3lv | 13720727502736428047 | 4.7 / 7 |
| Digos | https://share.google/ZhR7nN7OZBvad3uE2 | 14870322002658986799 | 5.0 / 2 |
| Gensan | https://share.google/cGydQQ7SYYZsivHlo | 8893155102601741404 | 5.0 / 1 |

Ratings are snapshots observed 14 September 2026, explicitly dated on the page, not live feed claims. No review quotes were copied or invented. Links open each branch's Google listing. The embedded map is Google's own UI and loads third-party Google content; a directions link remains available if it fails. Facebook is a branded direct-link panel, not an embedded feed or automatic Messenger submission.

Matina's more complete address was taken from its resolved Google listing: Door 5, MS Land Complex, Km 3 McArthur Highway, Talomo, Davao City. Opening-hour sources conflicted, so visitors are asked to confirm with the clinic rather than displaying guessed hours.

### Still needed before launch

Confirm all clinical copy, staff information, payment methods and hours with the clinic. Obtain approved current photos for Matina, Digos and Gensan; until then those pages link to their own Facebook photos rather than displaying another branch's interior. Blog remains omitted. Keep prototype noindex and private until the clinic approves use of its brand and campaign assets.
