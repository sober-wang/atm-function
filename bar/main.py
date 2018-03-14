#ATM机入口
#作者：尚墨
#邮箱：ws1992jx@163.com
#日期：2018年3月13日

import json
import getpass

def adron(fun):
    #使用装饰器实现用户登录认证
    def unt(*args,**kwargs):
        with open(*args) as msg:
            msg_lod = json.load(msg)
            #print(msg_lod)
            username = msg_lod['username']
            password = msg_lod['password']
        inpt_username = input("Please UserName:")
        inpt_password = getpass.getpass("Please Password:")
        if inpt_username == username and inpt_password == password:
            fun(*args,**kwargs)
        else:
            print("UserName and Password ERROR!")
    return unt

@adron
def welcom(msgf):
    #欢迎标语
    print('welcome to CRS!')

def selectfunction():
    fct = ['购物','取款','还款','查询']
    n = 1
    print("请选择你想使用的功能：")
    for ct in fct:
        print("%s:%s"%(n,ct))
        n +=1
    user_n = input("请选择想用的功能：")
    return user_n