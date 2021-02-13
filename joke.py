import requests

URL = 'https://icanhazdadjoke.com/search'

term = input('Term of your joke? ')

with requests.get(URL, headers={"accept": "application/json"}, params={'term': term, 'limit': 1}) as res:
    data = res.json()
    print(f'Jokes found with term \'{data["search_term"]}\' total found {data["total_jokes"]}', (
        '\n' + data['results'][0]['joke'] + ' 😂️🤣️😎️😁️') if len(data['results']) else "")
