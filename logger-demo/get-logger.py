#!/usr/bin/python3
from wxpy import get_wechat_logger

# 获得一个专用 Logger
# 当不设置 `receiver` 时，会将日志发送到随后扫码登陆的微信的"文件传输助手"
logger = get_wechat_logger()

# 发送警告
logger.warning('这是一条 WARNING 等级的日志，你收到了吗？')

# 接收捕获的异常
try:
    1 / 0
except:
    logger.exception('现在你又收到了什么？')
