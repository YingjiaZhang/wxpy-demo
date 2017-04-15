#!/usr/bin/python3
from wxpy import *
bot = Bot()
myfriend = bot.friends().search('莓')[0]
group = bot.groups().search('测试1')[0]
@bot.register(myfriend,msg_types=CARD)
def reply_my_friend(msg):
    print('5555' + msg);
    msg.chat.send_raw_msg(msg.raw['MsgType'], msg.raw['Content'])
print('12345678')
embed()

