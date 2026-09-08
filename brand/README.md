# Playworks North logo

Direction revised again 2026-09-08 (Eddy, after seeing a ChatGPT emblem with a GPS arrow): **a GPS navigation arrow pointing north**. A heading cursor is a notched triangle, so it reads as north, direction and a play button in one shape, with no gamepad. Eddy found the plain north star too generic and the emblems too complex. Bias toward a compass-rose star with a longer north ray so it is not a generic sparkle. The play-button drafts in `concepts/` are superseded. One
mark, no text needed at avatar size. Burnt orange (`#c8502c`) on cream
(`#f6f3ec`), cream on dark (`#16150f`), matching the site palette.

## Decision 2026-09-08 (evening)

Eddy picked the **square-notch arrow** (Envato batch 2, right tile) and asked for a
different colour. Colour is Claude's call: **glacier teal** `#0f8f87` on cream
`#f6f3ec`, brightened to `#2fd0c3` on navy `#0b1622`. Burnt orange was only
ever the site accent; the site should move to teal in one CSS change (see TODO).

## Files

- `mark/mark.svg` : the mark alone, teal. Source of truth, hand-drawn geometry:
  `M0,-46 L34,34 L9,34 L9,20 L-9,20 L-9,34 L-34,34 Z` on a 120 viewBox.
- `mark/mark_on_cream.svg`, `mark/mark_on_dark.svg`, `mark/badge_teal.svg`,
  `mark/badge_navy.svg` : dressings. `arrow_sheet.png` shows all four plus the
  badges at 32 px and 16 px; the notch survives at 16 px.
- `wordmark/` : the lockups, text outlined to paths so no font is needed.
  `lockup_light.svg` (mark left, ink text on cream) and `lockup_dark.svg`
  (cream text, bright teal on navy) are the primary; `stacked_*` puts the mark
  above the text for square spaces; `*_mono*` are single colour with no
  background. `wordmark_sheet.png` shows all four with backgrounds.
- Still to make: `favicon.ico`, `avatar-512.png`, `social-1200x630.png`.

## Wordmark 2026-09-08

Typeface **Sora** (OFL, SemiBold for PLAYWORKS at 0.05 em tracking, Medium for
NORTH at 0.30 em). Picked over Montserrat (wider, generic) and Outfit (close
second): Sora's squarer letters echo the square notch in the mark. PLAYWORKS
cap height 42 against the mark's 80, NORTH cap height 15 between two 3 unit
teal rules spanning the PLAYWORKS width. Still legible at 160 px wide.

Regenerate with `python3 brand/tools/lockup.py <outdir> sora` (needs Inkscape
and the Sora variable font in `~/.local/share/fonts`, fetched from the
google/fonts repo). The script outlines the text through Inkscape, so the
committed SVGs carry paths only.
- The earlier play-button concepts were deleted.

## Envato session 2026-09-08

Signed in at app.envato.com (Generate, Graphic mode, Solid background, 3 variations = 3 credits). Session "Burnt Orange North Star Logo": https://app.envato.com/generate/10bbe3b7-ed2d-46bc-a1e6-faa9f53b1620. Batch 1 (north star) came back as plain symmetric four-point stars, discard. Batch 2 (GPS arrow) produced two clean marks: a classic notched heading arrow and a narrower one with a square notch. One tile failed. 10 credits left, plan resets 2026-09-09. Next: redraw the notched arrow as SVG (it is four points and a notch, no tracing needed), test at 16 px, then wordmark.

## Envato AI prompts (needs Eddy signed in to Envato Elements in Chrome)

Tool: elements.envato.com/ai/ai-image-generator, style "Logo" or "Vector"
if offered, square, 3 variations per prompt. Use the vector draft as a
reference image where the tool accepts one.

1. Minimal flat vector logo mark, a four-pointed north star with a longer top ray, compass rose style, single solid burnt orange shape on an off-white
   background, no text, no gradient, no outline, centred, lots of negative
   space, geometric, app icon style.
2. Same as 1, cream shape on a near-black background.
3. Logo for an indie game studio called Playworks North, a single north star mark, flat vector, two colours only (burnt orange and
   cream), wordmark "Playworks North" in a clean geometric sans below the
   mark, no other elements.
4. Exploration: the same north star mark drawn with soft rounded
   corners, friendly but not childish, flat vector, single colour.

Judge results at 16 px before anything else. Anything that only works large
is a poster, not a logo. Vectorise the pick (Inkscape trace or redraw from
the draft geometry) so the final asset is an SVG, never a raster.

## Where the logo goes once final

GitHub org avatar, itch.io playworksnorth profile, Bluesky avatar, site
favicon and social preview (both open in `TODO.md`, "v1 follow-ups"), and
later the Steam publisher page.
