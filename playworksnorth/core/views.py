import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .forms import ContactForm
from .recaptcha import verify_recaptcha

logger = logging.getLogger(__name__)

PROJECTS = [
    {
        'name': 'EdNoKa',
        'kind': _('Game'),
        'status': _('Released'),
        'blurb': _('A word-building puzzle game where you carve new words out of old ones.'),
        'url': 'https://store.steampowered.com/app/3256100/',
        'link_label': 'Steam',
        'image': 'core/projects/ednoka.jpg',
    },
    {
        'name': 'Zenith Caller',
        'kind': _('App'),
        'status': _('In development'),
        'blurb': _('A coaching companion that turns training plans into daily, doable steps.'),
        'url': 'https://zenithcaller.com',
        'link_label': _('Site'),
        'image': 'core/projects/zenith-caller.svg',
    },
    {
        'name': 'It Shall Pass',
        'kind': _('Game'),
        'status': _('In development'),
        'blurb': _('A quiet game about breathing, attention, and letting the noise settle.'),
        'url': '',
        'link_label': '',
        'image': 'core/projects/it-shall-pass.svg',
    },
    {
        'name': 'ThirdAngle',
        'kind': _('Game assets'),
        'status': _('Released'),
        'blurb': _('Isometric pixel art asset packs for game makers, starting with a classroom and a science lab.'),
        'url': 'https://thirdangle.itch.io',
        'link_label': 'itch.io',
        'image': 'core/projects/thirdangle.png',
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
        'form': ContactForm(),
        'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY,
    })


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            token = request.POST.get('g-recaptcha-response', '')
            if verify_recaptcha(token, request.META.get('REMOTE_ADDR')):
                try:
                    EmailMessage(
                        subject=_('New message from %(name)s via playworksnorth.com') % {'name': form.cleaned_data['name']},
                        body=form.cleaned_data['message'],
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        to=[settings.CONTACT_RECIPIENT_EMAIL],
                        reply_to=[form.cleaned_data['email']],
                    ).send()
                    messages.success(request, _('Thanks, your message is on its way.'))
                except Exception:
                    logger.exception('Failed to send contact form email')
                    messages.error(request, _('Something went wrong sending your message. Please try again shortly.'))
            else:
                messages.error(request, _('The captcha check failed. Please try again.'))
        else:
            messages.error(request, _('Please fill in every field and try again.'))
    return redirect(f"{reverse('core:home')}#contact")
