import matplotlib.pyplot as plt
import numpy as np

#-----------------视觉图分析----------------------------------
# a = np.array([[3,104],
#              [2,100],
#              [1,81],
#              [101,10],
#              [99,5],
#              [98,2]])
# for i in range(3):
#     plt.plot([18,a[i,0]],[90,a[i,1]],color='r')
#     plt.scatter([18,a[i,0]],[90,a[i,1]],color='r')
# for i in range(3,6):
#     plt.plot([18,a[i,0]],[90,a[i,1]],color='b')
#     plt.scatter([18, a[i, 0]], [90, a[i, 1]], color='b')
# plt.scatter(18,90 ,color='y')
# plt.show()


# ------------KNN算法核心代码--------------------------
def KNN(inX, dataSet, labels, k):
    '''  参数使用说明
    :参数 inX:用于分类的输入向量    c
    :参数 dataSet:输入的训练样本集  a
    :参数 labels:标签向量           b
    :参数 k:用于选择最邻近的数目    4
    :返回值return:分类结果
    '''
    dataSetSize = dataSet.shape[0]   #shape获取dataSet的行列数，结果为6
    print('dataSetSize:',dataSetSize)
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet  #第1步：计算已知类别数据集中的点与当前点之间的距离
    print(np.tile(inX, (dataSetSize, 1)))
    print('diffMat:\n',diffMat)
    sqDiffMat = diffMat**2
    print('sqDiffMat:\n',sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1)
    print('sqDistances:\n',sqDistances)
    distances = sqDistances**0.5
    print('distances:\n',distances)
    sortedDistIndicies = distances.argsort()  #第2步：从小到大排序
    print("sortedDistIndicies",sortedDistIndicies)
    classCount={} #第3步选取与当前点距离最小的k个点
    for i in range(k): # i = 3
        voteIlabel = labels[sortedDistIndicies[i]]
        print("voteIlabel：",voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1  #第4步确定前k个点所在类别的出现频率
        print('classCount：',classCount)
    print('items:',classCount.items())
    sortedClassCount = list(classCount.items())  ##第5步返回前k个点出现频率最高的类别作为当前点的预测分类
    print('sortedClassCount:',sortedClassCount)
    sortedClassCount.sort(key = lambda x:x[1], reverse=True)
    print(sortedClassCount)
    print(sortedClassCount[0][0])
    return sortedClassCount[0][0]

a = np.array([[3,104],
             [2,100],
             [1,81],
             [101,10],
             [99,5],
             [98,2]])
b = ['爱情片','爱情片','爱情片','动作片','动作片','动作片']
c = np.array([18,90])
result_lab = KNN(c,a,b,4)
print(result_lab)



#------------------部分函数解析--------------------
#shape方法解析：shape函数是属于numpy库中array对象的方法
#用途：读取数据对象的行数和列数，以元组的形式返回
# print(a.shape)
# print(a.shape[0])
# print(b.shape)

#tile方法解析：
#功能是将数组重复n次，构成一个新的数组
# e = np.array([[1,2,3]])
# f = np.array([[1,2,3],[2,3,4]])
# print('e的结果为：\n',np.tile(e,2))
# print('f的结果为：\n',np.tile(f,2))
#假如我们输入一个元组(1,2)，我们会得到一个什么结果？
# print('f的结果为：\n',np.tile(f,(2,2)))

#sum方法解析：sum函数是属于numpy库中array对象的方法
#功能：求和
# g = np.array([[1,2,3],[9,8,7]])
# print(g.sum())          #axis=None，将数组/矩阵中的元素全部加起来，得到一个和。
# print(g.sum(axis=1))    #  axis=1，将每一行的元素相加,将矩阵压缩为一列，
# print(g.sum(axis=0))    #  axis=0，将每一列的元素相加,将矩阵压缩为一行

#argsort方法解析,属于numpy库中array对象的方法
# 功能：返回数组值从小到大的索引值
# h =  np.array([3, 1, 2])
# print(h.argsort())

#sort方法:对列表进行排序
# x =[4, 6, 2, 1, -7, 9]
# x.sort()
# x.sort(reverse = True)
# x.sort(key = abs)
# x.sort(key = abs,reverse = True)
# print(x)
# d = {'张三':89,'李四':92,'王五':87}
# d_list = list(d.items())
# print(d_list)
# d_list.sort(key = lambda x:x[1],reverse = True)
# print(d_list)
