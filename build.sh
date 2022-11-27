#!/bin/bash
#build the project

echo "Building..........."
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
