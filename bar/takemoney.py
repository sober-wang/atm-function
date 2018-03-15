#取款
#日期:2018年3月14日
#作者：尚墨
#邮箱：ws1992jx@163.com

import json
from datetime import datetime

def tkm(msgf,logdir):
    '''
    取款功能实现，会提示，可余额
    :param msgf:
    :param logdir:
    :return:
    '''
    with open(msgf,'r') as msg:
        msg_lod = json.load(msg)
    print("当余额：%s"%msg_lod['nowlimt'])
    if int(msg_lod['nowlimt']) == 0:
        print("您账户上已经没有余额，不可取钱")
        return "no"
    tkm_nmb = input("您需要取多少钱：")
    now_nmb = msg_lod['nowlimt'] - int(tkm_nmb)
    print("您当前余额为：%s"%now_nmb)
    msg_lod['nowlimt'] = now_nmb
    msg_lod['debt'] = -int(tkm_nmb)
    logfile = '%s%s'%(logdir,r'\takemoney.log')
    tkm_time = datetime.now()
    #print(tkm_time)
    logmsg = '[%s] 取款%s,剩余%s。\n'%(tkm_time,tkm_nmb,now_nmb)
    with open(logfile,'a',encoding='utf-8') as wrt_f:
        wrt_f.write(logmsg)
    with open(msgf,'w') as nowmg:
        json.dump(msg_lod,nowmg)