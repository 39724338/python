str1='千山鸟飞绝'
str2='万径人踪灭'
str3='孤舟蓑笠翁'
str4='独钓寒江雪'
list1=[list(str1),list(str2),list(str3),list(str4)]
# print(list1[1][0])
print('横版')
for i in range(4):
    for j in range(5):
        if j!=4:
            print(list1[i][j],end='')
        else:
            print(list1[i][j])
list1.reverse()
list2=[]
for j in range(5):
    for i in range(4):
        if i!=3:
            list2[j][i] = list1[i][j]
            print(list2[j][i],end='')
        else:
            list2[j][i] = list1[i][j]
            print(list2[j][i])
