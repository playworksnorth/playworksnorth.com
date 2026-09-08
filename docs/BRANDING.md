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
| 3 | ApexCoach | Ships next, has a LICENSE | Nothing yet |
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
