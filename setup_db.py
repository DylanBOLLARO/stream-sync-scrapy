import requests
import json
from dotenv import dotenv_values

config = dotenv_values("./../.env")
backend_url = config['NEXT_PUBLIC_BACKEND_URL']

url = f"{backend_url}/movie"

f = open('./movies.json')
movies = json.load(f)

for movie in movies:
    movie['image'] = movie['images'][0]['path']
    response = requests.request("POST", url, data=movie)