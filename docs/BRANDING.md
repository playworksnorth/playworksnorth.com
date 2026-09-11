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
      `application/copyright="© <year> Playworks North Studio"` on every preset.
- [ ] Any HTML5 export template with an `owner` or `author` string.

### Repo files
- [ ] `LICENSE` copyright line.
- [ ] `README.md` copyright or ownership paragraph.
- [ ] Contact email in user-facing code and templates (contact@playworksnorth.com
      for studio mail; project mailboxes stay as they are).

### In the product
- [ ] Credits screen or about dialog names Playworks North.
- [ ] Website footer: "© <year> Playworks North Studio" (French pages:
      "© <year> Studio Playworks North") or "a Playworks North project".
- [ ] Marketing posts use the studio name wherever the storefront already does.
      Reddit Indie Sunday titles must match the Steam developer field, so that
      post copy changes only after Steam does.

## Copyright wording before registration

Until the Quebec enregistrement exists, "Playworks North" is a trade name used
by Edouard Murat, not a legal entity. Two options for copyright lines:

- `© 2026 Playworks North` (short, matches what players see)
- `© 2026 Edouard Murat, doing business as Playworks North` (legally precise)

Decided 2026-09-09: `© 2026 Playworks North`.

Filed 2026-09-10: the trade name registered with the Registraire des entreprises
is "Studio Playworks North", with "Playworks North Studio" as its English version
(reference 020200137407928, pending the Registraire's name analysis). A French
generic is mandatory in front of an English name (REQ guide IN-531, section 5.3),
so bare "Playworks North" cannot be registered unless it becomes a
CIPO-registered trademark. The business is still Edouard Murat's sole
proprietorship (NEQ 2278365210) with no separate legal personality, so the
copyright holder is still Edouard Murat.

Decided 2026-09-10, replacing the 2026-09-09 call: copyright lines follow the
registered name. English: `© 2026 Playworks North Studio`. French:
`© 2026 Studio Playworks North`. LICENSE files, README paragraphs and Godot
export presets are English, so they take the English form; a bilingual surface
(this site's footer) uses each form on its own language. The brand players see
stays plain Playworks North: the site header, store pages and the
playworksnorth.com domain do not change. If the Registraire refuses the name,
copyright lines follow whatever name replaces it.

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


## Where contact@playworksnorth.com actually lives (settled 2026-09-09)

The site's contact form mails contact@playworksnorth.com, and for a day that
address existed nowhere reachable: IONOS had created a Mail Basic mailbox for
it on 2026-09-08, but the MX was switched to Google (smtp.google.com) the same
day, so mail routed to Workspace, where no such user, alias or group existed.
Messages were accepted by the relay and then dropped, and the bounce went to
the same dead address, so nothing was ever seen.

Fixed 2026-09-09 by adding contact@playworksnorth.com as an **alternate email
(alias) on the single Workspace user**, whose primary address is
contact@ednoka.com. That user now holds:

- contact@ednoka.com (primary)
- contact@godothire.com (alias, pre-existing)
- contact@playworksnorth.com (alias, added 2026-09-09)

So **contact form mail lands in the contact@ednoka.com inbox**, not in
edouardmurat1@gmail.com. That stays true until the Workspace primary domain
switches to playworksnorth.com, at which point these addresses just swap roles.

Outgoing mail for the form uses the Workspace SMTP relay service (Gmail >
Routing > SMTP relay service), whose rule already allowlists the site's server
74.208.9.220 (listed there as "GodotHire server"), with no SMTP auth. That is
why the form needs no mail password. Django points EMAIL_HOST at
smtp-relay.gmail.com; the only secrets in the server .env are the reCAPTCHA
keys.

Authentication records added at IONOS 2026-09-09, all three verified live:

- SPF    TXT @                    v=spf1 include:_spf.google.com ~all
- DKIM   TXT google._domainkey    2048-bit key generated in Admin console
                                  (Gmail > Authenticate email), published
                                  byte-for-byte and then switched on with
                                  "Start authentication"
- DMARC  TXT _dmarc               v=DMARC1; p=none; rua=mailto:contact@playworksnorth.com

DMARC is deliberately p=none (monitor only) to start. Move it to p=quarantine
and then p=reject once the rua reports show only legitimate senders passing;
tightening it before that would send real mail to spam.

Reading the rua reports. They arrive as a ZIP holding one XML file, named
<reporter>!<domain>!<start epoch>!<end epoch>.zip, one per reporter per UTC
day. Unzip and read the XML: each <record> is one sending IP, <count> is how
many messages it sent, and the pair that matters is <policy_evaluated> (did
DKIM and SPF pass *and* align with the header From) next to <auth_results>
(the raw result and which domain it was checked against). DMARC passes if
either column aligns and passes, so a DKIM pass alone is a pass.

First report, google.com for 2026-09-09 (received 2026-09-10): 4 messages,
all from Google outbound IPs, DKIM pass and aligned on all 4, so 100% DMARC
pass and no sign of anyone spoofing the domain. Three of the four also passed
SPF. The fourth was SPF neutral because its envelope sender was on ednoka.com,
whose SPF record is "v=spf1 include:mailgun.org a mx ?all" and so neither
authorises Google's servers nor aligns with a playworksnorth.com From. That is
the alias showing through: the one Workspace user is contact@ednoka.com and
playworksnorth.com hangs off it, so some paths still stamp the envelope with
the primary domain. It disappears when playworksnorth.com becomes the primary
domain, and the ednoka.com SPF record should gain include:_spf.google.com
regardless (see docs/dns/ednoka.com.txt) since that domain sends through
Workspace today and is neutral for every message it sends.

A report only exists for a day the domain sent mail. Admin console > Reporting
> Email Log Search, custom search, sender "playworksnorth.com", last 7 days,
run 2026-09-11: 4 messages, all on 2026-09-09 (contact-form tests, two from
contact@ and two from website@), nothing on 2026-09-10 or 2026-09-11. The
contact form is the domain's only sender, so reports stay rare until real
visitors use it, and "wait for more clean days" can wait a long time.

Delivery was still not the end of it. Once the alias existed, Gmail accepted
the form mail and then filed it as spam, logged verbatim as "blatant spam"
in Admin console > Reporting > Email Log Search. Cause: the form sent From
and To the same address (contact@playworksnorth.com), carrying a stranger's
Reply-To and free text from a public form, which reads as spoofing. Fixed
2026-09-09 by sending as website@playworksnorth.com, an address with no
mailbox (the relay allows any address in the domain), and Eddy marked the
trapped messages as not spam.

Email Log Search is the tool for any future "where did that mail go" question:
it shows the SMTP conversation, the delivery result, and the spam verdict per
recipient, which the sending side cannot see. A form that reports success only
proves the relay accepted the message, not that anyone received it.
