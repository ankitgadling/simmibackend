#!/bin/bash
#build the project

echo "Building..........."
python --version
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
