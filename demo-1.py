#!/usr/bin/python3
from wxpy import *
bot = Bot()
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    if 'wxpy' in msg.text.lower():
        f = bot.accept_friend(msg.card)
        f.send('哈哈，我自动接受了你的好友请求')
        g = bot.groups().search('测试1')[0]
        if f in g:
	        f.send('您已加入 {} 分组'.format(g.name))
        else:
#注意：如果该用户已经存在在这个分组，则会报异常
            g.add_members(f,'nihao')
embed()

