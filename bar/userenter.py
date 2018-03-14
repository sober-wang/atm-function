#用户登录认证

import json

username = 'sober'
password = ''

def unt(msgf):
    with open(msgf,'r') as msg:
        msg_lod = json.load(msg)
        print(msg_lod)