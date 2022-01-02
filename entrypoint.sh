#!/bin/sh

## Do whatever you need with env vars here ...
yes | ./manage.py search_index --rebuild

# Hand off to the CMD
exec "$@"