#程序入口


import os
import sys

#获取程序根路径：
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#把程序根路径加入环境变量
sys.path.append(BASE_DIR)

from bar import main

main.welcom()