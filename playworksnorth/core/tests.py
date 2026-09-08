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
