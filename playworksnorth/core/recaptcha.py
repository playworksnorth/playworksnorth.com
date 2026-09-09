import json
import urllib.parse
import urllib.request

from django.conf import settings

VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'


def verify_recaptcha(token, remote_ip=None):
    if not token:
        return False
    data = urllib.parse.urlencode({
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': token,
        'remoteip': remote_ip or '',
    }).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(VERIFY_URL, data=data), timeout=5) as resp:
            result = json.loads(resp.read().decode())
    except (OSError, ValueError):
        return False
    return bool(result.get('success'))
