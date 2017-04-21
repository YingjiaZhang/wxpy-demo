#!/usr/bin/env python3
from wxpy import *
import logging

logging.basicConfig(level=logging.INFO)

# 减少网络层日志的干扰
for m in 'requests', 'urllib3':
    logging.getLogger(m).setLevel(logging.WARNING)

bot = Bot(cache_path=True)

@bot.register()
def print_others(msg):
    print(msg.type)
    print(msg.raw)
    print(msg.file_name)
    msg.get_file('./data/' + msg.file_name)
    print('===============')
embed()
