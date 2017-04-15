#!/usr/bin/python3
from wxpy import *
bot = Bot();
# do something
g = bot.groups().search('测试1')[0]
f = bot.friends().search('yry')[0]
if f in g:
	f.send('您已加入 {} 分组'.format(g.name))
else:
#注意：如果该用户已经存在在这个分组，则会报异常
    g.add_members(f,'nihao')
embed()
