# Playworks North branding checklist

How a project comes to "live under" Playworks North. Scope is public branding
only: repos stay under the StrayEddy GitHub account and local folders stay
where they are (Eddy, 2026-09-08). Projects move one at a time, most exposed
first. Track the studio-wide items in `TODO.md` here under "Studio admin", and
the per-project items in that project's own `TODO.md` so its board shows them.

## Roster and order

| Order | Project | Why here | Public today |
| --- | --- | --- | --- |
| 1 | EdNoKa | Live on Steam, Next Fest in October | Steam (3256100, demo 5182400, DLC 4344180), ednoka.com |
| 2 | ThirdAngle | Live on itch.io | thirdangle.itch.io |
| 3 | Zenith Caller | Ships next, has a LICENSE | zenithcaller.com |
| 4 | It Shall Pass | In development | Nothing yet |
| 5 | Everybody Hates Monday | In development | Nothing yet |
| 6 | GodotHire | Live site, no attribution today | godothire.com |

Not studio projects: godot-gridforge, HiveCell, SeedCell, JobSearchHelper,
edouardmurat.com.

## Per-project checklist

Copy the relevant lines into the project's `TODO.md`. Skip a line when the
surface does not exist yet, and add it back the day the surface appears.

### Storefronts
- [ ] Steam: developer and publisher fields say Playworks North on every app id
      (base, demo, DLC). Changing the publisher name in Steamworks is a support
      ticket, not a form field. Tracked in the site TODO under "Studio admin".
- [ ] itch.io: page shows "by Playworks North", or the project's own identity
      is a deliberate decision recorded in its TODO.
- [ ] App stores: publisher display name only. **Never change an iOS bundle
      identifier or an Android package name**: a new identifier is a new app
      with no reviews, no installs and no ratings carried over.

### Build metadata (Godot)
- [ ] `export_presets.cfg`: `application/company_name="Playworks North"` and
      `application/copyright="© <year> Playworks North"` on every preset.
- [ ] Any HTML5 export template with an `owner` or `author` string.

### Repo files
- [ ] `LICENSE` copyright line.
- [ ] `README.md` copyright or ownership paragraph.
- [ ] Contact email in user-facing code and templates (contact@playworksnorth.com
      for studio mail; project mailboxes stay as they are).

### In the product
- [ ] Credits screen or about dialog names Playworks North.
- [ ] Website footer: "© <year> Playworks North" or "a Playworks North project".
- [ ] Marketing posts use the studio name wherever the storefront already does.
      Reddit Indie Sunday titles must match the Steam developer field, so that
      post copy changes only after Steam does.

## Copyright wording before registration

Until the Quebec enregistrement exists, "Playworks North" is a trade name used
by Edouard Murat, not a legal entity. Two options for copyright lines:

- `© 2026 Playworks North` (short, matches what players see)
- `© 2026 Edouard Murat, doing business as Playworks North` (legally precise)

Decision pending in the site `TODO.md`. Until decided, leave existing lines as
they are.

## Studio-wide surfaces (not per project)

- GitHub org profile: avatar, description, URL.
- itch.io playworksnorth profile.
- Bluesky handle via DNS TXT record.
- Steam publisher name (support ticket, covers all EdNoKa app ids at once).
- Logo, in progress 2026-09-08.

## Google Workspace (studio mail under one roof)

Proposed 2026-09-08, waiting on Eddy. Today the Workspace has ednoka.com as
primary domain and godothire.com as a secondary domain, while
contact@playworksnorth.com is an IONOS mailbox. Domains are free in Workspace,
only user seats cost, so the whole studio fits in the one account.

Target: playworksnorth.com primary, ednoka.com and godothire.com secondary,
every product address an alias or a Google Group on one paid user.

Order, so no mail is lost:

1. Admin console, Account, Domains, Manage domains: add playworksnorth.com as
   a **secondary domain** (not an alias), verify with the TXT record at IONOS.
   The domain stays registered at IONOS; only mail moves.
2. Create contact@playworksnorth.com in Workspace first, as an alias on the
   main user or as a Group with a collaborative inbox.
3. At IONOS DNS: replace the MX for playworksnorth.com with Google's single
   MX (smtp.google.com), add Google's SPF and DKIM and a DMARC record, remove
   the IONOS mail records. Send a test. Forward or download anything in the
   IONOS mailbox, then delete it.
4. Change the primary domain to playworksnorth.com (allow up to 48 h).
   Existing addresses keep working; ednoka.com becomes secondary.
5. Rename the main user to eddy@playworksnorth.com (the old address becomes an
   alias) and set the organisation name to Playworks North.
6. Audit seats: if contact@ednoka.com or the GodotHire address are separate
   paid users, fold them into aliases or groups.

Primary-domain change is supported on Business editions, not on the legacy
free edition or on subscriptions bought through a reseller. The site's A
records and the Bluesky TXT record are unaffected. The auto-created guest
domain and test alias rows in the Domains list can be ignored.

## Consolidating accounts (started 2026-09-08)

Target: three places. IONOS for domain registrations, DNS and both servers.
Google Workspace for every mailbox. GitHub for code.

Inventory 2026-09-08: Squarespace holds the registrations for ednoka.com,
godothire.com and edouardmurat.com (DNS edited there, on Google nameservers).
IONOS holds playworksnorth.com plus two servers: the VPS 74.208.9.220 serves
playworksnorth.com, godothire.com and edouardmurat.com; a second server
74.208.184.11 serves ednoka.com. Mail: ednoka.com and godothire.com on
Workspace, edouardmurat.com on Mailgun, playworksnorth.com on Workspace (MX
live 2026-09-08, SPF, DKIM, DMARC and the contact@ alias still to do).

Order:
1. Finish the playworksnorth.com mail move (section above).
2. Registrar transfers Squarespace to IONOS, one domain at a time:
   edouardmurat.com first as the rehearsal, then godothire.com, then
   ednoka.com. Before each transfer, recreate its DNS records at IONOS (A,
   Google MX, SPF, DKIM, verification TXT) so nothing blinks when the
   nameservers switch. Unlock at Squarespace, get the auth code, start the
   transfer at IONOS, approve the email. A few days each, adds a year.
3. Close the Squarespace account.
4. Change the Workspace primary domain to playworksnorth.com.

Decide on the way: edouardmurat.com mail (fold into Workspace unless an app
sends through Mailgun). The second server is out of scope for this cleanup.

Progress 2026-09-08: docs/dns/ holds the full record list of each domain as
read from the Squarespace panel. All three domains are unlocked at Squarespace
and their transfer codes requested (Squarespace emails them to the registrant,
edouardmurat1@gmail.com). IONOS contracts: 106801127 "VPS Linux M" is the
74.208.9.220 server (edouardmurat.com and godothire.com go there), 102502184
"VPS Linux L" is the ednoka.com server. The IONOS transfer flow
(my.ionos.com/domainshop/transfer?contract=...) asks for the auth code up
front, prices a .com transfer at $9.50 for the first year, then $20/year, and
adds a year to the registration.

Transfers started 2026-09-08 (order confirmations from IONOS for all three,
Squarespace emails say each transfer completes on its own by 2026-09-13
unless cancelled). IONOS was told to switch each domain to its own name
servers on arrival, and Squarespace deletes the zone at that moment, so the
records must be recreated at IONOS the day each domain lands:

1. my.ionos.com/domain-dns-settings/<domain>: delete the IONOS defaults
   (parking A/AAAA, IONOS MX, autodiscover CNAMEs).
2. Add every line from docs/dns/<domain>.txt except the _domainconnect CNAME
   and the stale dv.googlehosted.com CNAMEs. ednoka.com and godothire.com
   need the five Google MX, SPF, the google-site-verification TXT(s), and
   for ednoka.com the google._domainkey DKIM TXT. edouardmurat.com needs the
   two Mailgun MX, SPF and k1._domainkey.
3. Check with `dig +short <domain> A`, `MX`, `TXT`, and www.
4. Turn on IONOS domain lock (Domain Guard is optional, it is a paid add-on).

