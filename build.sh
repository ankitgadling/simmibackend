#!/bin/bash
#build the project

echo "Building..........."
python3.10 -m pip install -r requirements.txt
python3.10 manage.py collectstatic --noinput --clear