# Server layout (IONOS VPS, Ubuntu, root)

Captured 2026-09-07 from the live box. The same server hosts edouardmurat.com and godothire.com; playworksnorth.com mirrors edouardmurat.com's wiring. Host address is the one in the deploy workflow.

## Existing pattern (edouardmurat.com)

- Checkout: `/root/edouardmurat.com`, venv at `/root/edouardmurat.com/venv`, Django project dir `edouardmurat/` inside it.
- Gunicorn systemd unit `/etc/systemd/system/edouardmurat.service`: User=root, Group=www-data, WorkingDirectory=`/root/edouardmurat.com/edouardmurat`, 3 workers, bind `unix:/run/edouardmurat.sock`, app `edouardmurat.wsgi:application`.
- nginx vhost in `/etc/nginx/sites-enabled/`: `location /static/` aliases the app's static dir, `location /` proxies to the socket with `include proxy_params`. Certbot manages the 443 block and the 80 redirect.
- Deploy key: the ed25519 pair on the server whose public half is in authorized_keys as `github-actions-deploy`. Its private half is the `SSH_PRIVATE_KEY` GitHub Actions secret. Never stored in this repo.
- Deploy workflow: on push to main, SSH in, `git pull`, `pip install -r requirements.txt`, `collectstatic`, `systemctl restart <service>`.

## Target for playworksnorth.com

- Checkout `/root/playworksnorth.com`, venv `/root/playworksnorth.com/venv`, project dir `playworksnorth/`.
- Unit `playworksnorth.service`, socket `/run/playworksnorth.sock`, app `playworksnorth.wsgi:application`.
- nginx vhost `playworksnorth.com www.playworksnorth.com`, static alias `/root/playworksnorth.com/staticfiles/` (collectstatic target, the godothire style).
- HTTPS: `certbot --nginx -d playworksnorth.com -d www.playworksnorth.com` once DNS resolves.

Files for the unit and vhost live in this directory; a one-time bootstrap script installs them.
