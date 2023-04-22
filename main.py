import random
import time
from datetime import datetime
import json

import telebot

with open('config.json', encoding='utf-8') as config_file:
    config = json.load(config_file)
    TOKEN = config['TOKEN']
    CHAT_ID = config['CHAT_ID']

bot = telebot.TeleBot(TOKEN)


def get_compliment():
    with open('config.json', encoding='utf-8') as config_file:
        config = json.load(config_file)
        return random.choice(config['COMPLIMENTS'])


def send_compliment():
    compliment = get_compliment()
    print(compliment)
    bot.send_message(CHAT_ID, compliment)

    with open('logs.txt', 'a', encoding='utf-8') as file:
        file.write(f'{datetime.now()}, The message has been sent, text: {compliment}\n')


while True:
    try:
        send_compliment()
    except:
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(f'{datetime.now()}, Sending failed\n')
    time.sleep(3600)
