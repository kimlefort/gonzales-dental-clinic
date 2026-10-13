---
name: Gonzales Dental website proposal
description: A warm editorial site for a family dental practice
colors:
  practice-green: "#143d2d"
  deep-green: "#0e2f23"
  warm-gold: "#c6aa70"
  ivory: "#f7f4ec"
  ink: "#183b2d"
  muted: "#657269"
  divider: "#d9ded3"
typography:
  display:
    fontFamily: "Manrope, sans-serif"
    fontSize: "clamp(42px, 5.05vw, 78px)"
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-3.9px"
  headline:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: "clamp(36px, 4vw, 58px)"
    fontWeight: 500
    lineHeight: 1.12
    letterSpacing: "-2.2px"
  body:
    fontFamily: "DM Sans, Arial, sans-serif"
    fontSize: "15px"
    lineHeight: 1.6
  label:
    fontFamily: "DM Sans, Arial, sans-serif"
    fontSize: "10px"
    fontWeight: 600
    letterSpacing: "2.2px"
rounded:
  button: "3px"
  filter: "30px"
spacing:
  section-desktop: "100px"
  section-mobile: "62px"
components:
  button-ivory:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.practice-green}"
    rounded: "{rounded.button}"
    padding: "14px 24px"
  button-gold:
    backgroundColor: "{colors.warm-gold}"
    textColor: "{colors.deep-green}"
    rounded: "{rounded.button}"
    padding: "14px 24px"
---

# Design System: Gonzales Dental website proposal

## Overview

**Creative North Star: "The Family Portrait"**

The site pairs published family and clinic photography with an editorial green, ivory, and gold layout. Large headings establish a calm, confident first impression; small labels and fine dividers organize the detail. This is a working design direction for the private proposal, subject to the clinic's approval.

**Key Characteristics:** original practice imagery; strong typography; direct branch contact; restrained ornament.

## Colors

Practice green and deep green carry the major hero and contact surfaces. Warm gold marks emphasis and primary contact actions. Ivory is the page ground; ink, muted green, and pale dividers support reading and structure.

## Typography

Manrope provides the strong heading hierarchy, DM Sans handles body copy and labels, and Cormorant Garamond adds a softer italic accent to selected heading lines. Keep the italic face as an accent so the factual copy remains easy to scan.

## Layout

Sections use generous desktop spacing and narrower mobile gutters. Desktop service and story areas use two columns; clinic cards use four columns, then two and one at smaller widths. The header becomes a compact menu below 850px, with a fixed contact action at the bottom of the screen. The major mobile layout shift occurs at 760px.

## Elevation & Depth

The system is mostly flat. Dark and light surface changes, fine borders, and photography carry depth. The mobile contact bar has a small shadow to separate it from content while scrolling.

## Shapes

Buttons use 3px corners. Filter controls are pill shaped with a 30px radius. Cards and content panels stay square and use lines or subtle surface changes for definition.

## Components

- **Contact buttons:** ivory in the hero, gold in the contact panel and mobile bar; keep the action wording aligned with the direct phone or message flow.
- **Filters:** outlined pills with a solid green selected state and `aria-pressed` state.
- **Service rows:** divided accordion summaries with a plus icon and direct treatment links inside.
- **Clinic cards:** a selected card gets a pale green surface and a visible selected label; branch choice updates contact details and map together.
- **Navigation:** the green sticky header carries the logo, page links, and branch picker; a menu replaces page links on narrow screens.

## Do's and Don'ts

### Do:

- **Do** use real clinic and family imagery with clear captions and attribution.
- **Do** keep branch-specific contact details together and make the selected branch visible.
- **Do** make touch actions at least 44px tall.

### Don't:

- **Don't** imply that the site confirms an appointment; patients call or message the clinic.
- **Don't** present dated review snapshots as live ratings.
- **Don't** add unsupported treatment outcomes or staff claims.
