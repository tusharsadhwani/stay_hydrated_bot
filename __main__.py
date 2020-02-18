from datetime import datetime
from pytz import timezone
from time import sleep
from telegram import Bot

from message_hour import MessageTimer

india = timezone('Asia/Kolkata')
indian_time = datetime.now(tz=india)

with open('token.txt') as f:
    token = f.read().strip()

msg_timer = MessageTimer(indian_time)

while True:
    if msg_timer.msg_hour == indian_time.hour:
        Bot(token=token).send_message(170256543, text="Remember to stay hydrated :3")
        msg_timer.increment()
        print('Next message at hour', msg_timer.msg_hour)
    sleep(60)