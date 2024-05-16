#!/bin/bash

docker exec -ti stream-sync-backend npx prisma db push --force-reset

python3 -m venv venv

source venv/bin/activate

pip3 install -r stream-sync-scrapy/requirements.txt

scrapy crawl allocine -o movies.json

python3 ./stream-sync-scrapy/setup_db.py

docker compose -f compose.dev.yml up -d