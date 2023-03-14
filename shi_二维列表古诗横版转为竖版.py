str1='千山鸟飞绝'
str2='万径人踪灭'
str3='孤舟蓑笠翁'
str4='独钓寒江雪'
list1=[list(str1),list(str2),list(str3),list(str4)]
print('---------列表显示------------')
print(list1)
print('---------横版显示------------')
for i in range(4):
    for j in range(5):
        if j==4:
            print(list1[i][j])
        else:
            print(list1[i][j],end='')
list1.reverse()
print('----------转置列表显示--------')
print(list1)
print('----------测试显示--------')

print('----------竖版显示--------')
for j in range(5):
    for i in range(4):
        if i==3:
            print(list1[i][j])
        else:
            print(list1[i][j],end='')
