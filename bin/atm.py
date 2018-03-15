#程序入口


import os
import sys

#获取程序根路径：
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#把程序根路径加入环境变量
sys.path.append(BASE_DIR)

from bar import main
from bar import selectMammey
from bar import takemoney
from bar import repay

CONF_DIR = '%s%s'%(BASE_DIR,r'\conf\atmuser.txt')
#print(CONF_DIR)
LOG_DIR = '%s%s'%(BASE_DIR,r'\log')
while True:
    sltnmb = main.welcom(CONF_DIR)
    if int(sltnmb) == 4:
        selectMammey.bln(CONF_DIR)
    elif int(sltnmb) == 2:
        t_vlue = takemoney.tkm(CONF_DIR,LOG_DIR)
        if t_vlue == 'no':
            sys.exit()
    elif int(sltnmb) == 3:
        repay.rpy(CONF_DIR,LOG_DIR)
    elif sltnmb == 'q':
        print('Good bye!')
        break