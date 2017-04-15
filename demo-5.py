#!/usr/bin/python3
from wxpy import *
bot = Bot()
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
#    print('auto_accept_friends')
    f = bot.accept_friend(msg.card)
    f.send('提示 list :  \n1.聊天\n 2.加群 \n请回复编号：(例如:1)')
    @bot.register(f)
    def auto_reaponse(msg):
#        print('auto_response')
        if msg.text == '1':
            f.send('挖掘机技术哪家强？')
            @bot.register(f)
            def print_reply(msg):
                print(msg.text)
                if msg.text == '#':
                    return auto_reaponse(msg)
                else:
                    return msg.text
        if msg.text == '2':
            g = bot.groups().search('c1')[0]
            if f not in g:
                g.add_members(f,'nihao')
embed()

