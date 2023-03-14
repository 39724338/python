def fun_checkout(money):
    '''功能：计算商品的合计金额
    money:保存商品的金额列表
    返回值：商品的合计金额和折扣后的金额'''
    money_old=sum(money)
    money_new=money_old
    if 500<money_old<1000:
        money_new="{:.2f}".format(money_old*0.9)
    elif 1000<=money_old<=2000:
        money_new="{:.2f}".format(money_old*0.8)
    elif 2000<money_old<=3000:
        money_new="{:.2f}".format(money_old*0.7)
    elif money_old > 3000:
        money_new = "{:.2f}".format(money_old * 0.6)
    return money_old,money_new
print('\n开始结算****\n')
list_money=[]
while True:
    inmoney=float(input('请输入商品金额：' ))
    if int(inmoney)==0:
        break
    else:
        list_money.append(inmoney)
    money=fun_checkout(list_money)
print('合计金额',money[0],'应付金额',money[1])