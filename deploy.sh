#!/bin/bash
set -e

cd /home/ubuntu/Photos-website
git pull

source venv/bin/activate
pip install gunicorn
python manage.py collectstatic --noinput

# Kill existing runserver
sudo pkill -f 'manage.py runserver' || true

# Install dependencies
sudo apt update
sudo DEBIAN_FRONTEND=noninteractive apt install -y nginx certbot python3-certbot-nginx

# Setup Gunicorn
sudo tee /etc/systemd/system/gunicorn.service <<'EOF'
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Photos-website
ExecStart=/home/ubuntu/Photos-website/venv/bin/gunicorn --access-logfile - --workers 3 --bind 127.0.0.1:8000 config.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl enable gunicorn

# Setup Nginx
sudo tee /etc/nginx/sites-available/photos <<'EOF'
server {
    listen 80;
    server_name ai-measurement.sahabaplus.com;
    client_max_body_size 50M;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    # We must use alias since the directory is named staticfiles but the URL is /static/
    location /static/ {
        alias /home/ubuntu/Photos-website/staticfiles/;
    }
    
    location /media/ {
        alias /home/ubuntu/Photos-website/media/;
    }

    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://127.0.0.1:8000;
    }
}
EOF

sudo ln -sf /etc/nginx/sites-available/photos /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
