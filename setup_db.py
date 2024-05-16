import requests
import json

url = "http://stream-sync-backend:5000/api/v1/movie"

f = open('./movies.json')
movies = json.load(f)

for movie in movies:
    movie['image'] = movie['images'][0]['path']
    response = requests.request("POST", url, data=movie)