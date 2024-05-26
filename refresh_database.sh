#!/bin/bash

docker exec -ti stream-sync-backend npx prisma db push --force-reset

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

scrapy crawl allocine -O movies.json

python3 setup_db.py

docker compose -f ./../compose.dev.yml --env-file ./../.env up -d