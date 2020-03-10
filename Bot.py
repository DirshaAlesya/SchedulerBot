import schedule
import time
import requests
import os


def bot_sendtext():
    bot_token = os.environ.get('TOKEN')
    bot_chatID = os.environ.get('CHATID')
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=Доброе утро!'

    requests.get(send_text)

schedule.every().day.at("07:00").do(bot_sendtext)

while True:
    schedule.run_pending()
    time.sleep(1)
