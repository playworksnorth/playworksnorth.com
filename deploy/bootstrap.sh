#!/usr/bin/env bash
# One-time server setup for playworksnorth.com. Run as root on the VPS:
#   curl -fsSL https://raw.githubusercontent.com/playworksnorth/playworksnorth.com/main/deploy/bootstrap.sh | bash
# Safe to re-run.
set -euo pipefail

REPO=https://github.com/playworksnorth/playworksnorth.com.git
DIR=/root/playworksnorth.com

apt-get install -y -q gettext >/dev/null

if [ ! -d "$DIR/.git" ]; then
  git clone "$REPO" "$DIR"
fi
cd "$DIR"
git pull

[ -d venv ] || python3 -m venv venv
venv/bin/pip install -q -r requirements.txt

if [ ! -f .env ]; then
  printf 'DJANGO_SECRET_KEY=%s\nDJANGO_DEBUG=0\n' "$(venv/bin/python -c 'from django.core.management.utils import get_random_secret_key as k; print(k())')" > .env
  chmod 600 .env
fi

venv/bin/python playworksnorth/manage.py compilemessages -l fr
venv/bin/python playworksnorth/manage.py collectstatic --no-input

cp deploy/playworksnorth.service /etc/systemd/system/playworksnorth.service
systemctl daemon-reload
systemctl enable --now playworksnorth.service
systemctl restart playworksnorth.service

cp deploy/nginx-playworksnorth.conf /etc/nginx/sites-available/playworksnorth.com
ln -sf /etc/nginx/sites-available/playworksnorth.com /etc/nginx/sites-enabled/playworksnorth.com
nginx -t && systemctl reload nginx

certbot --nginx -n --agree-tos --redirect --keep-until-expiring \
  -d playworksnorth.com -d www.playworksnorth.com \
  --email "${CERTBOT_EMAIL:-edouardmurat1@gmail.com}" || echo "certbot failed; run it by hand once DNS is live"

echo "Done. https://playworksnorth.com"
