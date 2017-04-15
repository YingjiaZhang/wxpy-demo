#!/usr/bin/python3
from wxpy import *
bot = Bot()
friends = bot.friends().search('yry')
group = bot.create_group(friends,'测试3')
group.send('hello!')
embed();



