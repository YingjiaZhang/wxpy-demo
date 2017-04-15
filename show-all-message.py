#!/usr/bin/python3

from wxpy import *

bot = Bot()

@bot.register()
def print_messages(msg):
    print(msg)

embed()

