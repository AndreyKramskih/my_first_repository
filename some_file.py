import time

import requests


API_URL='https://api.telegram.org/bot'
API_CATS_URL='https://api.thecatapi.com/v1/images/search'
BOT_TOKEN='7656570135:AAHAU-5sKUFNc5UfgpBqEd4fxrKQWcQpoeU'



offset=-2
updates=dict

def do_something() ->None:
    print('Был апдейт')

while True:
    start_time=time.time()
    updates=requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()

    if updates['result']:
        for result in updates['result']:
            offset=result['update_id']
            do_something()
    time.sleep(3)
    end_time=time.time()
    print(f'Время между запросами к Telegram BOT API: {end_time-start_time}')
