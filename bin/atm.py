#程序入口


import os
import sys

#获取程序根路径：
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#把程序根路径加入环境变量
sys.path.append(BASE_DIR)

from bar import main
from bar import searchfct
from bar import selectMammey
from bar import userenter

CONF_DIR = '%s%s'%(BASE_DIR,r'\conf\atmuser.txt')
print(CONF_DIR)

main.welcom(CONF_DIR)
main.selectfunction()
#userenter.unt(CONF_DIR)
#sltnmb = searchfct.searchfct()
#print(sltnmb)

#if int(sltnmb) == 4:
#    selectMammey.bln(CONF_DIR)
#elif int(sltnmb) == 2:
#    pass