#!/usr/bin/python3
from wxpy import *
bot = Bot()
@bot.register()
def auto_accept_friends(msg):
    f = bot.accept_friend(msg.card)
    f.send('哈哈，我自动接受了你的好友请求')
    g = bot.groups().search('c1')[0]
    if f not in g:
        g.add_members(f,'nihao')
embed()

