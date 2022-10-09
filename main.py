import random

import requests

raw_jokes = open('jokes.txt', 'r').read().split('\n\n\n\n\n')

jokes = []
for joke in raw_jokes:
    joke = joke.strip().replace('\n\n', '\n')
    if not joke.isdigit():
        jokes.append(joke)

token = ""
owner_id = -216048905
from_group = 1
version_vk = "5.131"

url = "https://api.vk.com/method/wall.post"

response = requests.post(
    url=url,
    params={
        'access_token': token,
        'from_group': from_group,
        'owner_id': owner_id,
        'message': random.choice(jokes),
        'v': version_vk,
    }
)

print(response.json())
