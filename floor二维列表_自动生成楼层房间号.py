# 手动输入
# room=[[1101,1102,1103,1104,1105,1106,1107],[2101,2102,2103,2104,2105,2106,2107],[3101,3102,3103,3104,3105,3106,3107],
#       [4101,4102,4103,4104,4105,4106,4107]]
# print(room)

#利用for循环自动生成
# room=[]
# for i in range(1,5):#楼层
#     room.append([])
#     for j in range(1,7):#每层房间数
#         room[i-1].append(i*1000+100+j)
# print(room)

#利用列表推导式自动生成,方法1
# room=[[(1100+i) for i in range(1,8)],[(2100+i) for i in range(1,8)],[(3100+i) for i in range(1,8)],[(4100+i) for i in range(1,8)]]
# print(room)

#利用列表推导式自动生成,方法2
list0=list((1000*1+100+j) for j in range(1,8))
print(list0)
room=[list((1000*i+100+j) for j in range(1,8)) for i in range(1,7)]
print(room)
