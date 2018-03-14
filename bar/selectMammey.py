#查询余额

import json

def bln(msgf):
    with open(msgf,'r') as jsonf:
        msg_lod = json.load(jsonf)
        print(msg_lod['redumumy'])