# playworksnorth.com TODO

Studio site for Playworks North. This is the only task list for the `playworks-north/` workspace.

## Decisions needed
- [ ] Squarespace to IONOS transfers, all three started 2026-09-08 (edouardmurat.com, godothire.com, ednoka.com show Incoming transfer at IONOS; Squarespace completes them by itself unless cancelled before 2026-09-13). When each one lands: recreate its DNS at IONOS from docs/dns/<domain>.txt the same day (sites are dark and mail queues until then), then verify with dig. After all three: close the Squarespace account, decide edouardmurat.com mail (Mailgun or Workspace). Steps in docs/BRANDING.md, Consolidating accounts
- [ ] Google Workspace: make playworksnorth.com the primary domain, ednoka.com and godothire.com secondary, move contact@playworksnorth.com from IONOS into Workspace. Ordered steps in docs/BRANDING.md, Google Workspace section. Progress 2026-09-08: domain added as secondary and verification TXT set, IONOS mail service removed, MX smtp.google.com live. Progress 2026-09-09: contact@playworksnorth.com now exists as an alias on the contact@ednoka.com user, so mail to it is delivered. Progress 2026-09-09: SPF, DKIM (2048-bit, authentication started in Admin console) and DMARC (p=none) all added at IONOS and verified resolving. Left: watch the DMARC rua reports and move p=none to quarantine/reject once clean, then the primary domain switch
- [ ] Copyright wording before the Quebec registration exists: "© 2026 Playworks North" or "© 2026 Edouard Murat, doing business as Playworks North". Options in docs/BRANDING.md. Existing lines stay untouched until decided
- [ ] ThirdAngle on itch.io: keep the thirdangle identity as a standalone brand, or add "by Playworks North" to the profile and pack pages
- [x] 2026-09-09 Contact form (honeypot + reCAPTCHA v2 checkbox) replacing the mailto link Eddy flagged as bot bait. reCAPTCHA keys are in the server .env, mail goes out through the Workspace SMTP relay that already allowlists 74.208.9.220, so no mail password exists anywhere. contact@playworksnorth.com did not exist as a mailbox at all (IONOS made one 2026-09-08, then the MX moved to Google the same day and no Workspace address was ever created, so messages were silently dropped); fixed 2026-09-09 by adding it as an alias on the one Workspace user. Mail then delivered but was filed as spam because the form sent from and to the same address; now sends as website@playworksnorth.com with SPF/DKIM/DMARC in place. Details in docs/BRANDING.md
- [x] 2026-09-07 Hosting: the IONOS VPS (74.208.9.220) that already runs edouardmurat.com, Eddy's call
- [x] 2026-09-07 Scope of v1: single landing page (studio blurb, project cards, contact), Eddy can widen later

## v1
- [x] 2026-09-07 Stack: Django, same as edouardmurat.com (Eddy: all his websites use Django). Mirror its layout: project package + core app, gunicorn behind nginx as a systemd service, collectstatic on deploy
- [x] 2026-09-07 Landing page copy, EN and FR (first draft, placeholder blurbs for ApexCoach and It Shall Pass, please review)
- [x] 2026-09-07 Project cards (EdNoKa with Steam link, ThirdAngle with itch.io link, ApexCoach and It Shall Pass marked in development)
- [x] 2026-09-08 Contact link uses contact@playworksnorth.com (the IONOS mailbox made that day stopped receiving once the MX moved to Google; the address is a Workspace alias since 2026-09-09, and the link itself became a form the same day)
- [x] 2026-09-08 Server bootstrapped by Eddy, site is live at https://playworksnorth.com in EN and FR over HTTPS
- [x] 2026-09-07 GitHub Actions deploy workflow (.github/workflows/deploy.yml); first run fails until bootstrap has cloned the repo on the server
- [x] 2026-09-07 IONOS DNS: A records for @ and www point at the VPS, verified resolving
- [x] 2026-09-07 SSH_PRIVATE_KEY secret set on the GitHub repo


## v1 follow-ups
- [x] 2026-09-08 EN button did nothing from the French page: Django's set_language cannot translate /fr/ back to / when the default language is unprefixed. Switcher is now plain links to the translated URL, with a regression test in core/tests.py
- [x] 2026-09-08 Site accent moved to the logo teal (#0f8f87 light, #2fd0c3 dark, links use a darker #0c7a73 on cream for contrast), mark inline in the header next to the name
- [ ] Verify the EdNoKa Steam link points at the right app (3256100)
- [x] 2026-09-08 Favicon (ico, svg, apple-touch-icon), Open Graph and Twitter card tags, social preview image; also added the i18n context processor so the html lang attribute is no longer empty
- [ ] Review EN/FR copy in playworksnorth/core/views.py and locale/fr
- [x] 2026-09-09 Project cards redesigned: real key art per card (EdNoKa's Steam header, ThirdAngle's itch.io cover) or a branded placeholder (Zenith Caller, It Shall Pass), whole card is the link with a hover lift, no separate Steam/Site button. Deployed. The first grid was wrong on desktop (auto-fit gave 3 columns for 4 cards, stranding the last one), now an explicit 1/2-column grid
- [x] 2026-09-09 It Shall Pass card art is now the game's real logo, not a placeholder: the torii mark with its amber ember, on the game's own night field. Colours are GamePalette entries rather than the studio teal (night blue #101428 to #0A0A14, neon violet #E26CC6, ember #F0A860; recoloured off cyan the same day because cyan sat too close to Zenith Caller's teal), so the card looks like the game and not like the site. Source of truth for the mark is it-shall-pass/art/brand/icon.svg; if that changes, this card needs the same edit
- [x] 2026-09-09 Zenith Caller card art off the studio teal and onto the project's own colour (Eddy: every card uses its own project's palette, not the site's). **Updated later the same day to the finished mark**, which is no longer provisional: ZenithCaller settled its icon on 2026-09-09 (the hexagon, one shape at three scales, hollow shifted down 8, approved as drawn), so the card now carries that whole mark instead of the chevron alone. Colour is the project's mint #6fcdb0 on its own badge ground #0f1317; the red-orange the first version used is gone, and the Apex red was tried and rejected in ZenithCaller itself on legal grounds, so it must not come back here. The path in the card is copied verbatim from ZenithCaller/art/brand/icon.svg, which is generated by art/brand/build_icon.py; if the mark is retuned there, this file needs the same edit
- [ ] Swap both placeholder cards (Zenith Caller, It Shall Pass) for real screenshots once each has one. The logo cards are a better placeholder, not the final answer
- [x] 2026-09-09 Project card renamed ApexCoach -> Zenith Caller, now links to https://zenithcaller.com (new "Site" button label, translated in locale/fr). The blurb is still the 2026-09-07 placeholder and does not describe the app (a live voice coach for Apex Legends), so it is covered by the copy review above

## Studio admin (not site work, tracked here for now)
- [x] 2026-09-08 Branding migration scoped: public branding only, repos and folders stay put. Roster: EdNoKa, ThirdAngle, ApexCoach, It Shall Pass, Everybody Hates Monday, GodotHire. Order and checklist in docs/BRANDING.md; per-project items live in each project's TODO.md
- [ ] Logo for Playworks North: direction chosen 2026-09-08 (north star as a play button), three vector drafts in brand/concepts with a comparison sheet, Envato prompts in brand/README.md. Envato run done 2026-09-08: direction is now a GPS heading arrow pointing north (two good raster candidates in the Envato session, link in brand/README.md). Mark chosen and drawn 2026-09-08: square-notch arrow in glacier teal, brand/mark/mark.svg, passes the 16 px test. Wordmark lockups done 2026-09-08 in Sora, brand/wordmark (horizontal, stacked, light, dark, mono). Export set done 2026-09-08 in brand/export (favicon, avatars 512 and 1024, social 1200x630) and wired into the site. Left: upload avatar-512.png to the GitHub org, itch.io profile and Bluesky (see the admin items below)
- [ ] Quebec registry name check (Registraire des entreprises), then enregistrement
- [ ] Bluesky handle to @playworksnorth.com via DNS TXT record at IONOS, and set the avatar to brand/export/avatar-512.png
- [ ] Change EdNoKa's Steam developer and publisher name to Playworks North (support ticket in Steamworks, covers 3256100, demo 5182400 and DLC 4344180 at once). Until this lands, Reddit Indie Sunday titles keep "Edouard Murat" because the rule is to match the Steam field
- [ ] Fill in GitHub org profile (avatar brand/export/avatar-512.png, description, URL)
- [ ] Fill in itch.io playworksnorth profile (avatar brand/export/avatar-512.png)

## Done
- [x] 2026-09-07 Name research (domains, Steam, CIPO trademarks): Playworks North chosen
- [x] 2026-09-07 playworksnorth.com bought on IONOS
- [x] 2026-09-07 GitHub org, itch.io and Bluesky accounts created
- [x] 2026-09-07 Repo created
