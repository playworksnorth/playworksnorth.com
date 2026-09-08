# playworksnorth.com TODO

Studio site for Playworks North. This is the only task list for the `playworks-north/` workspace.

## Decisions needed
- [x] 2026-09-07 Hosting: the IONOS VPS (74.208.9.220) that already runs edouardmurat.com, Eddy's call
- [ ] Scope of v1: single landing page (studio blurb, project cards for EdNoKa / ApexCoach / meditation game, contact) vs. multi-page

## v1
- [x] 2026-09-07 Stack: Django, same as edouardmurat.com (Eddy: all his websites use Django). Mirror its layout: project package + core app, gunicorn behind nginx as a systemd service, collectstatic on deploy
- [ ] Landing page copy, EN and FR
- [ ] Project cards with links (EdNoKa Steam page, ApexCoach)
- [ ] Contact link (email) and social links (Bluesky, itch.io, GitHub org)
- [ ] Server setup on the VPS: nginx vhost for playworksnorth.com, checkout in /root/playworksnorth.com, venv, gunicorn systemd unit (playworksnorth.service), certbot for HTTPS
- [ ] GitHub Actions deploy workflow (same shape as edouardmurat.com: SSH in, git pull, pip install, collectstatic, restart playworksnorth.service); needs SSH_PRIVATE_KEY secret on the org repo
- [ ] IONOS DNS: A record for playworksnorth.com and www pointing at 74.208.9.220


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
