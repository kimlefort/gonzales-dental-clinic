# Gonzales Dental website proposal

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Prospective and returning patients looking for a treatment, a nearby Gonzales Dental clinic, and a direct way to arrange a visit. This is the working audience assumption for the proposal; the clinic has not yet approved it.

The proposal is also shown to Gonzales Dental decision makers, who need to judge whether the site represents the practice accurately and helps patients contact the right branch.

## Product Purpose

Explain the practice, treatments, and four clinics, then help a visitor choose a branch and contact it by phone, Facebook, or email. Success for this proposal means the clinic can see a credible path from first impression to a branch-specific inquiry. The site does not itself confirm appointments.

## Operating Context

Visitors may arrive on a phone, look up a treatment or location, read FAQs, and use external Google Maps or Facebook links. Selecting a branch updates the displayed contact details, map, and review snapshot.

## Capabilities and Constraints

- Django-rendered website with a homepage, About and History pages, FAQs, ten treatment pages, and four branch pages.
- Branch choice can be made in the header, clinic cards, or appointment section. Branch pages take precedence over a saved browser preference.
- Booking is handled directly by the selected clinic; there is no online booking endpoint.
- The current build is a private design proposal, marked `noindex,nofollow`, and has not been deployed.
- A Laplace Labs intro notice identifies the experience as a demo on first visit and can be reopened from the footer. It states that the photos, clinic locations and contact details are real.
- Clinic approval of wording, imagery rights, and current branch details remains open before public use.

## Brand Commitments

Use the Gonzales Dental name, its published three-generation history, and the original logo already included in the project. The current copy uses “Three Generations of Dental Care.” Brand approval remains open.

## Evidence on Hand

`clinic/content.py` holds the published branch, treatment, FAQ, and history content used by the site. `CONTENT_SOURCES.md` records attribution and preview limits. The project includes a published campaign portrait, portraits of family members, and a photograph of the Obrero waiting area. Review ratings are explicitly dated snapshots, not a live feed. Other branches link to their own Facebook photography because approved interior images are not in the project.

## Product Principles

- Make the selected clinic and its contact route clear at every point of inquiry.
- Keep published facts traceable and label information that may change.
- Present the family history as evidence of the practice, without adding unsupported claims.
- Preserve the direct-contact booking model until the clinic provides an actual booking system.
