from django.test import TestCase


class LanguageSwitchTests(TestCase):
    """The default language is unprefixed, so the URL prefix alone decides the
    language. The switcher must therefore link to the translated URL of the
    page rather than post to set_language, which cannot translate /fr/ back to
    / (it resolves the path under the active language, EN, where /fr/ does not
    exist)."""

    def test_english_page_links_to_french(self):
        r = self.client.get('/')
        self.assertContains(r, '<html lang="en"')
        self.assertContains(r, 'hreflang="fr" href="/fr/"')

    def test_french_page_links_back_to_english(self):
        r = self.client.get('/fr/')
        self.assertContains(r, '<html lang="fr"')
        self.assertContains(r, 'hreflang="en" href="/"')

    def test_following_the_english_link_serves_english(self):
        r = self.client.get('/', HTTP_ACCEPT_LANGUAGE='fr', HTTP_COOKIE='django_language=fr')
        self.assertContains(r, '<html lang="en"')


class CopyrightLineTests(TestCase):
    """The footer names the copyright holder by the trade name registered with
    the Registraire des entreprises du Québec, which has a French form and an
    English version, so each language gets its own. The brand in the header
    stays plain Playworks North."""

    def test_english_footer_uses_registered_english_name(self):
        r = self.client.get('/')
        self.assertContains(r, 'Playworks North Studio, Montreal.')

    def test_french_footer_uses_registered_french_name(self):
        r = self.client.get('/fr/')
        self.assertContains(r, 'Studio Playworks North, Montréal.')


class FrenchCatalogTests(TestCase):
    """Every project card string must have a French translation. The GodotHire
    card shipped in English on /fr/ for two months because its strings were
    never added to the catalog."""

    def test_every_project_card_is_translated(self):
        from django.utils import translation
        from .views import PROJECTS
        for p in PROJECTS:
            for key in ('kind', 'status', 'blurb'):
                with translation.override('en'):
                    english = str(p[key])
                with translation.override('fr'):
                    french = str(p[key])
                self.assertNotEqual(french, english, f"{p['name']} {key} has no French translation")


class SocialLinkTests(TestCase):
    def test_bluesky_links_to_the_domain_handle(self):
        r = self.client.get('/')
        self.assertContains(r, 'https://bsky.app/profile/playworksnorth.com"')
        self.assertNotContains(r, 'playworksnorth.bsky.social')
