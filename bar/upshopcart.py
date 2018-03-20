#作用：读取货单文件，输出商品编号和价格。产生工资余额记录文件
#作者：尚墨
#日期：2018年1月21日
#邮箱：ws1992jx@163.com

import os

def shopmsg(shmf):
    waybill = open(shmf,'r')
    wb_list = waybill.readlines()
    return wb_list
'''
shopcart = []

#利用os.path.exists()方法判断文件是否存在
if os.path.exists('./balance.txt') == False:
    tmp = open('./balance.txt','w')
    tmp.close()
else:
    pass
#只读模式读出balance文件中的内容，并赋值
bl_file = open('./balance.txt','r')
bl_money = bl_file.readline()
bl_file.close()

print(bl_money)
#判断balance文件内容是否可用
if bl_money == '':
    salay = int(input('请输入工资：'))
else:
    salay = int(bl_money)



while True:
    for idx,wb in enumerate(wb_list):
        print('%s号货品是：%s'%(idx,wb.strip()))
    select_wb = input("请输入货品编号挑选货物")
    if select_wb.isdigit():
        select_wb = int(select_wb)
        if select_wb >= 0 and select_wb < len(wb_list):
            wb_tmp,money = wb_list[select_wb].split(':')
            money = int(money.strip())
            print(wb_tmp,money)
            if money <= salay:
                salay = salay - money
                shopcart.append((wb_tmp,money))
                print('您花费%s,买下了%s,当前工资余额为%s'%(money,wb_tmp,salay))
            else:
                print('您当前余额不足，请等下个月发工资！！！当前余额为：%s'%salay)
        else:
            print('货架上没有%s号商品，请重新输入'%select_wb)
    elif select_wb == 'q':
        if len(shopcart) == 0:
            print("这么节俭，购物车都是空的！")
            break
        else:
            print('------您购买了如下货物--------')
            for wb_result in shopcart:
                print(wb_result)
            bl_value = str(salay)
            bl_file = open('./balance.txt','w')
            bl_file.write(bl_value)
            bl_file.close()
            break
    else:
        print('您输入的商品编号%s不合法，请重新输入'%select_wb)


waybill.close()
'''