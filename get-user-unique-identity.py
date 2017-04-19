#!/usr/bin/env python3
from wxpy import *
bot = Bot()

@bot.register()
def get_userinfo(msg):
    print(msg.sender)
    f = msg.sender
    info = f.raw
    print(info['Uin'])
embed()



