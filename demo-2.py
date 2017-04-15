#!/usr/bin/python3
from wxpy import *
bot = Bot()
friends = bot.friends().search('Z')
group  = bot.create_group(friends,'测试1')
@bot.register()
def auto_accept_friends(msg):
    if 'wxpy' in msg.text.lower():
        f = bot.accept_friend(msg.card)
        f.send('哈哈，我自动接受了你的好友请求')
        group = bot.groups().search('测试1')[0]
        if f in g:
	        f.send('您已加入 {} 分组'.format(group.name))
        else:
#注意：如果该用户已经存在在这个分组，则会报异常
            g.add_members(f,'nihao')

#@bot.register()
def print_others(msg):
    print(msg)
print('=============================================1')
#bot.register()
def auto_reply(msg):
   if msg.text == '1':
		   return '请回复您的地址：格式为　陕西西安'
   if msg.text == '陕西西安':
		   return '请回复您的姓名：eg : z'
   if msg.text == 'z':
		   return '挖掘机技术哪家强'
   return 'Please input try again!'

print('=============================================2')

embed()

