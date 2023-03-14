while True:                               #while循环
    matial=input("请加入披萨配料：")      #输入配料
    if matial=='quit':                    #用if判断输入的是quit
        break                              #break跳出循环
    else:
        print("您为披萨添加",matial,"配料")#输出添加的配料
