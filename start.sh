#!/bin/bash
cd /home/username/your_project_directory
export FLASK_APP=app.py
export FLASK_ENV=production
gunicorn --bind 0.0.0.0:8000 --workers 2 wsgi:app