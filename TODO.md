# playworksnorth.com TODO

Studio site for Playworks North. This is the only task list for the `playworks-north/` workspace.

## Decisions needed
- [x] 2026-09-07 Hosting: the IONOS VPS (74.208.9.220) that already runs edouardmurat.com, Eddy's call
- [x] 2026-09-07 Scope of v1: single landing page (studio blurb, project cards, contact), Eddy can widen later

## v1
- [x] 2026-09-07 Stack: Django, same as edouardmurat.com (Eddy: all his websites use Django). Mirror its layout: project package + core app, gunicorn behind nginx as a systemd service, collectstatic on deploy
- [x] 2026-09-07 Landing page copy, EN and FR (first draft, placeholder blurbs for ApexCoach and It Shall Pass, please review)
- [x] 2026-09-07 Project cards (EdNoKa with Steam link, ThirdAngle with itch.io link, ApexCoach and It Shall Pass marked in development)
- [x] 2026-09-07 Contact link (hello@playworksnorth.com, mailbox still to create at IONOS) and social links (Bluesky, itch.io, GitHub org)
- [x] 2026-09-08 Server bootstrapped by Eddy, site is live at https://playworksnorth.com in EN and FR over HTTPS
- [x] 2026-09-07 GitHub Actions deploy workflow (.github/workflows/deploy.yml); first run fails until bootstrap has cloned the repo on the server
- [x] 2026-09-07 IONOS DNS: A records for @ and www point at the VPS, verified resolving
- [x] 2026-09-07 SSH_PRIVATE_KEY secret set on the GitHub repo


## v1 follow-ups
- [ ] Create the hello@playworksnorth.com mailbox (or forward) at IONOS
- [ ] Verify the EdNoKa Steam link points at the right app (3256100)
- [ ] Favicon and social preview image
- [ ] Review EN/FR copy in playworksnorth/core/views.py and locale/fr

## Studio admin (not site work, tracked here for now)
- [ ] Quebec registry name check (Registraire des entreprises), then enregistrement
- [ ] Bluesky handle to @playworksnorth.com via DNS TXT record at IONOS
- [ ] Change EdNoKa's Steam publisher name to Playworks North
- [ ] Fill in GitHub org profile (avatar, description, URL)
- [ ] Fill in itch.io playworksnorth profile

## Done
- [x] 2026-09-07 Name research (domains, Steam, CIPO trademarks): Playworks North chosen
- [x] 2026-09-07 playworksnorth.com bought on IONOS
- [x] 2026-09-07 GitHub org, itch.io and Bluesky accounts created
- [x] 2026-09-07 Repo created
