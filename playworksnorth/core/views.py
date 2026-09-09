from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

PROJECTS = [
    {
        'name': 'EdNoKa',
        'kind': _('Game'),
        'status': _('Released'),
        'blurb': _('A word-building puzzle game where you carve new words out of old ones.'),
        'url': 'https://store.steampowered.com/app/3256100/',
        'link_label': 'Steam',
    },
    {
        'name': 'Zenith Caller',
        'kind': _('App'),
        'status': _('In development'),
        'blurb': _('A coaching companion that turns training plans into daily, doable steps.'),
        'url': 'https://zenithcaller.com',
        'link_label': _('Site'),
    },
    {
        'name': 'It Shall Pass',
        'kind': _('Game'),
        'status': _('In development'),
        'blurb': _('A quiet game about breathing, attention, and letting the noise settle.'),
        'url': '',
        'link_label': '',
    },
    {
        'name': 'ThirdAngle',
        'kind': _('Game assets'),
        'status': _('Released'),
        'blurb': _('Isometric pixel art asset packs for game makers, starting with a classroom and a science lab.'),
        'url': 'https://thirdangle.itch.io',
        'link_label': 'itch.io',
    },
]

SOCIALS = [
    {'label': 'Bluesky', 'url': 'https://bsky.app/profile/playworksnorth.bsky.social'},
    {'label': 'itch.io', 'url': 'https://playworksnorth.itch.io'},
    {'label': 'GitHub', 'url': 'https://github.com/playworksnorth'},
]

CONTACT_EMAIL = 'contact@playworksnorth.com'


def home(request):
    return render(request, 'core/home.html', {
        'projects': PROJECTS,
        'socials': SOCIALS,
        'contact_email': CONTACT_EMAIL,
    })
