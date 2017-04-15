#!/usr/bin/python3
from wxpy import *
bot = Bot();
# do something
tuling = Tuling(api_key='7239ce48844d414ba7a59ea5aa7dbacb')
# 使用图灵机器人自动与指定好友聊天
@bot.register()
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)

embed()

