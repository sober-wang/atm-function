#还款

import json
from datetime import datetime

def rpy(msgf,logdir):
    '''
    功能：还款函数，会提示欠款金额，已还多少，还欠多少:
    '''
    with open(msgf,'r') as msg:
        msg_lod = json.load(msg)
    print('您欠款数：%s'%msg_lod['debt'])
    rpy_mny = int(input('您想还多少：'))
    rm_tmp = rpy_mny + msg_lod['debt']
    print(rm_tmp)
    msg_lod['nowlimt'] = msg_lod['nowlimt'] + rpy_mny
    if rm_tmp > 0:
        msg_lod['debt'] = 0
    elif rm_tmp < 0:
        msg_lod['debt'] = rm_tmp
    with open(msgf,'w') as msg_w:
        json.dump(msg_lod,msg_w)
    logfile = '%s%s'%(logdir,r'\repay.log')
    logtime = datetime.now()
    logmsg = '%s 还款:%s 欠款数:%s\n'%(logtime,rpy_mny,msg_lod['debt'])
    with open(logfile,'a') as rpf:
        rpf.write(logmsg)