#!/bin/sh

./wait-for-it.sh es:9200
## Do whatever you need with env vars here ...
# python manage.py crontab add
yes | ./manage.py search_index --rebuild

gunicorn --bind 0.0.0.0:8000 project.wsgi
# Hand off to the CMD
# exec "$@"