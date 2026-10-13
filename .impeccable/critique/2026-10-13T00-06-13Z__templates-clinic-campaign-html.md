---
target: homepage campaign
total_score: 22
max_score: 32
na_heuristics: 7,9
p0_count: 0
p1_count: 2
target_identity: "file:/Users/stlorenz/Development/web_dev/gonzales-dental-github-ready/templates/clinic/campaign.html"
target_fingerprint: "sha256:3d1439d421f62813f9d8a5d758dd5f6ae8ea76280d4ecbcbd9875d8d46a2cea3"
target_path: /Users/stlorenz/Development/web_dev/gonzales-dental-github-ready/templates/clinic/campaign.html
timestamp: 2026-10-13T00-06-13Z
slug: templates-clinic-campaign-html
---
# Gonzales Dental campaign critique

Method: dual-agent (A: design_assessment · B: detector_assessment)

## Design Health Score

| # | Heuristic | Score | Key issue |
|---|---|---:|---|
| 1 | Visibility of system status | 3/4 | Branch changes update content, but lack an explicit confirmation. |
| 2 | Match with the real world | 2/4 | “Book a visit” suggests scheduling; the actual action is contacting the clinic. |
| 3 | User control and freedom | 3/4 | Branch choice and filters are reversible. |
| 4 | Consistency and standards | 3/4 | Visual and branch patterns are coherent. |
| 5 | Error prevention | 3/4 | Selected branch and contact details stay together. |
| 6 | Recognition rather than recall | 3/4 | Controls are labeled, but mobile loses its contact CTA after scrolling. |
| 7 | Flexibility and efficiency | n/a | Campaign surface. |
| 8 | Aesthetic and minimalist design | 3/4 | Strong hero; service exploration presents many choices at once. |
| 9 | Error recovery | n/a | No local data-entry workflow; map has directions fallback. |
| 10 | Help and documentation | 2/4 | FAQs exist, but booking and availability caveats are distant from the hero promise. |
| **Total** | | **22/32** | **Acceptable** |

## Design Specificity Verdict

The original logo, published portrait, named three-generation story, clinician portraits, Obrero interior, and four real branch contacts make this recognizably Gonzales Dental. The green, cream, gold, split portrait and italic serif treatment is coherent, though the most specific proof arrives below a broad hero promise.

The detector reported one `flat-type-hierarchy` warning at `templates/clinic/campaign.html:0`. It could not resolve the Django `{% static %}` stylesheet href and treated all headings as 16px. Browser computed sizes contradict the warning: at 1440px, body 15px, h1 72px, h2 57.6px, h3 22px; at 390px, body 15px, h1 39px, h2 37px, h3 22px. This warning is a false positive. CSS color and custom-property detector rules were incomplete for the same reason. Browser injection was unavailable through the documented read-only evaluation API, so no overlay was shown.

## Overall Impression

The site has a credible family-practice identity and a useful branch-aware contact flow. Its largest opportunity is to describe the appointment handoff accurately and keep that action visible on mobile.

## What's Working

- Published family and clinic evidence gives the practice specificity without invented testimonials.
- Changing Obrero to Matina updates the phone, Facebook, email, map and dated review snapshot together.
- Desktop and mobile hero/contact compositions are readable and focused.

## Priority Issues

1. **P1 — Clarify booking promise.** Header and hero say “Book a visit,” while the destination offers call, Facebook and email and says appointments are confirmed by the clinic. Patients may expect an online time selection. Change those CTAs to “Arrange a visit” or “Contact your clinic,” and explain the call/message handoff near the hero action. Suggested command: `$impeccable clarify`.
2. **P1 — Keep contact action visible on mobile.** At 390px the sticky header hides `.header-book`; after the hero, reaching contact requires scrolling through many sections or opening navigation. Add a compact persistent contact action that fits 320–390px without covering content. Suggested command: `$impeccable adapt`.
3. **P2 — Reduce service decision load.** Four ribbon categories are repeated by five filters and ten visible accordion summaries. Group common paths or reveal the full ten on request while retaining direct treatment links. Suggested command: `$impeccable distill`.
4. **P2 — Clarify branch location earlier.** Header options use short names, including “Gensan”; location context appears later. Show city-aware names where space permits and keep the selected branch obvious. Suggested command: `$impeccable clarify`.

## Persona Red Flags

- A first-time patient can read “Book” as a promise that a confirmed time follows.
- A distracted mobile patient loses the visible contact route once the hero is gone.
- A patient who changes to Matina still sees an Obrero interior section. It is labeled, but the branch context needs to remain unmistakable.

## Minor Observations

The dated review snapshot is disclosed, but a live Google Maps embed can display a newer rating beside it. Keep the checked date near the snapshot. The footer correctly labels the site as a private proposal.

## Questions to Consider

- Should branch choice happen before the first contact action?
- Could the family and clinician evidence move closer to the first viewport?
- Which contact channel can each clinic reliably respond to fastest?
