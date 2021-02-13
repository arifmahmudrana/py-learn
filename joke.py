import requests

URL = 'https://icanhazdadjoke.com/'

with requests.get(URL, headers={"accept": "application/json"}) as res:
    print(res.json()['joke'] + ' 😂️🤣️😎️😁️')
