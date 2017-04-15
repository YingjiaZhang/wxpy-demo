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


# 运行过程
# ./demo-1.py
#　首先 用你的微信创建一个分组名字为'测试1'
#  接下来 用你的微信扫一下弹出来的二维码　-> 登录成功
#  然后 用别人的微信添加你为好友，
#  如果别人输入的验证信息为 wxpy　则你会自己添加他为好友，
#  并判断他是否在'测试1'分组内:若在则发送提示信息，若不在则发送邀请信息。
