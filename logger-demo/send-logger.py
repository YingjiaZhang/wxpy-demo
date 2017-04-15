#!/usr/bin/python3
from wxpy import *
bot = Bot();
# do something
logger_reciver = bot.friends().search('Z')[0];
logger = get_wechat_logger(logger_reciver)
logger.error('你有一条新的告警，请查收。');
embed()

