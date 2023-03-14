age=int(input("请输入年龄："))                #定义变量age
if age>0 and age<=20:                         #判断年龄在0~20之间
    if age>0 and age<=13:                     #嵌套的if判断年龄在0~13之间
        print("您的年龄是:",age,",您是儿童")  #输出提示
    else:                                     #嵌套的else判断年龄在13~20之间
       print("您的年龄是:",age,",您是青少年") #输出提示
else:                                         #else判断年龄大于20之间
    if age>20 and age<=65:                    #嵌套的if判断年龄在20~65之间
        print("您的年龄是:",age,",您是成年人")#输出提示
    else:                                     #嵌套的else判断年龄在65以上之间
       print("您的年龄是:",age,",您是老年人") #输出提示
    
