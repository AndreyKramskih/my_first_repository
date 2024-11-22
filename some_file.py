import time

import requests

API_URL='https://api.telegram.org/bot'
BOT_TOKEN='7656570135:AAHAU-5sKUFNc5UfgpBqEd4fxrKQWcQpoeU'
TEXT='Ура, классный апдейт!'
MAXCOUNTER=100

offset=-2
counter=0
chat_id:int

while counter < MAXCOUNTER:
    print('attempt =', counter) #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()

    if updates['result']:
        for result  in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
    time.sleep(1)
    counter+=1