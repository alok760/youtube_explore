#!/bin/sh

## Do whatever you need with env vars here ...
# python manage.py crontab add
yes | ./manage.py search_index --rebuild

# Hand off to the CMD
exec "$@"