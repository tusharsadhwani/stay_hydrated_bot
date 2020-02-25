from datetime import datetime
from pytz import timezone
from time import sleep
from telegram import Bot

from message_hour import MessageTimer
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

india = timezone('Asia/Kolkata')

with open('token.txt') as f:
    token = f.read().strip()

msg_timer = MessageTimer(tz=india)

while True:
    indian_time = msg_timer.get_current_time()
    print("Current hour:", indian_time.hour, "\t Next Message at", msg_timer.msg_hour)
    if msg_timer.msg_hour == indian_time.hour:
        Bot(token=token).send_message(170256543, text="Remember to stay hydrated :3")
        msg_timer.increment()
        print('Next message at hour', msg_timer.msg_hour)
    sleep(60)