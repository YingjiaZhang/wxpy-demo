#!/usr/bin/env python3
import requests
r = requests.get('http://10.22.64.36:3000/wechat?str=wszl')
print(r.text)



