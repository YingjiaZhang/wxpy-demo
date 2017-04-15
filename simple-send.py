#!/usr/bin/env python3
from wxpy import *
bot = Bot();
my_friend = bot.friends().search('莓')[0];
my_friend.send('请回复1');
@bot.register()
def print_others(msg):
   print(msg)

@bot.register(my_friend)
def reply_my_friend(msg):
   if msg.text == '1':
		   return '请回复您的地址：格式为　陕西西安'
   if msg.text == '陕西西安':
		   return '请回复您的姓名：eg : z'
   if msg.text == 'z':
		   return '挖掘机技术哪家强'
   return 'Please input try again!'

embed()



