#!/bin/sh

ssh root@103.108.140.130 <<EOF
  cd /var/www/html/adsproject/classified/
  git pull
  cd /var/www/html/adsproject/
  source adsenv/bin/activate
  cd classified/
  cat requirements.txt | xargs -n 1 pip install
  python manage.py migrate
  sudo systemctl restart gunicorn
  exit
EOF