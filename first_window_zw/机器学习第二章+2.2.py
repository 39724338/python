import numpy as np

#------------------从文件中读取数据为数组--------------------
def file2matrix(filename,feature_num):
    '''
    :param filename: 输入需要读入的文件名称，如果文件不在代码相同的目录下，需要输入完整的路径名+文件名
    :feature_num：特征个数
    :return:训练集数据和样本标签，是数组类型

    '''
    fr = open(filename)
    numberOfLines = len(fr.readlines()) #获取文件的行数
    # print(numberOfLines)
    returnMat = np.zeros((numberOfLines,feature_num))
    # print(returnMat)
    classLabelVector = []    #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        # print(line, type(line))
        line = line.strip()
        # print(line, type(line))
        listFromLine = line.split('\t')
        # print(listFromLine)
        returnMat[index,:] = listFromLine[0:feature_num]
        classLabelVector.append(int(listFromLine[feature_num:][0]))
        index += 1
    # print(returnMat,classLabelVector)
    return returnMat,classLabelVector
feature_data, label_data  = file2matrix('datingTestSet2.txt',3)

# -------------归一化特征值——————————
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m,1))
    normDataSet = normDataSet/np.tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals

# new_feature,ranges,minvalus = autoNorm(feature_data)
# print(new_feature,ranges,minvalus)

# -------------KNN——————————
def KNN(inX, dataSet, labels, k):
    '''  参数使用说明
    :参数 inX:用于分类的输入向量    c
    :参数 dataSet:输入的训练样本集  a
    :参数 labels:标签向量           b
    :参数 k:用于选择最邻近的数目    4
    :返回值return:分类结果
    '''
    dataSetSize = dataSet.shape[0]   #shape获取dataSet的行列数，结果为6
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet  #第1步：计算已知类别数据集中的点与当前点之间的距离
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()  #第2步：从小到大排序
    classCount={} #第3步选取与当前点距离最小的k个点
    for i in range(k): # i = 3
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1  #第4步确定前k个点所在类别的出现频率
    sortedClassCount = list(classCount.items())  ##第5步返回前k个点出现频率最高的类别作为当前点的预测分类
    sortedClassCount.sort(key = lambda x:x[1], reverse=True)
    return sortedClassCount[0][0]

#-------------------------测试KNN数据------------
def datingClassTest():
    hoRatio = 0.10  # hold out 10%
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt',3)  # load data setfrom file
    m = datingDataMat.shape[0]    #m  = 1000
    numTestVecs = int(m * hoRatio)     #numTestVecs  = 100
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = KNN(datingDataMat[i, :], datingDataMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("KNN测试结果为: %d, 实际值为: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print("总的错误率为: %f" % (errorCount / float(numTestVecs)))
    print(errorCount)

def datingClassTest_new():
    hoRatio = 0.10  # hold out 10%
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt',3)  # load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = KNN(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("KNN测试结果为: %d, 实际值为: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("总的错误率为: %f" % (errorCount / float(numTestVecs)))
    print(errorCount)

# datingClassTest_new()

#-----------通过已经确定好的KNN模型，获取结果------------------
def classify_result():
    result_list = ['不喜欢','普通 ','非常喜欢']
    travel = float(input('请输入每年旅行的路程:'))
    game_time = float(input('请输玩游戏所占百分比:'))
    junkfood = float(input('请输入每个礼拜消耗的零食重量kg:'))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt', 3)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inputarry = np.array([travel,game_time,junkfood])
    result_num = KNN((inputarry-minVals)/ranges,normMat,datingLabels,3)
    print('赵六对这个人是{}'.format(result_list[result_num-1]))
classify_result()




#------------------matplotlib绘制--------------------
# settings -->Tools --> Python Scientific修改图形展示窗口
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# plt.scatter(feature_data[:,0],label_data ,color='r')
# plt.title('KNN 展示',fontproperties='SimHei')
# plt.plot(feature_data[:,0],feature_data[:,1],'b' '.')
# plt.xlabel('x轴',fontproperties='SimHei')
# plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
# # print(label_data)
ax.scatter(feature_data[:,0],feature_data[:,1] ,feature_data[:,2],s = 10,c =label_data)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# plt.show()








#------------------部分函数解析--------------------
#zeros方法解析：zeros函数是属于numpy库中的方法
#用途：返回来一个给定形状和类型的用0填充的数组
# a = np.zeros((4,3))
# print(a)

#--------------matplotlib演示----------------------
# import matplotlib.pyplot as plt  #matplotlib.pyplot是绘制各种图形的命令子库
# fig = plt.figure()
# plt.plot([1,2,3,6],[4,5,8,1],'r''s')
# plt.scatter([1,2,3,6],[4,5,8,1],s = 100,c= 'r',marker = 'o')

# plt.show()