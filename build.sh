#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py seed_parties
python manage.py seed_more_parties
python manage.py seed_actionsa
python manage.py seed_eff
python manage.py seed_commentary
python manage.py seed_extra_commentary
