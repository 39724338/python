from numpy import *
import operator
def createDateSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

# a = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
# b = a.shape
# print(b)

# k-近邻算法
#inX：用于分类的输入向量  dataSet：输入的训练样本集    labels：标签向量     K；用于选择最邻近的数目
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]   #shape获取dataSet的行列数
    print('dataSetSize:',dataSetSize)
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    print(tile(inX, (dataSetSize, 1)))
    print('diffMat:',diffMat)
    sqDiffMat = diffMat**2
    print('sqDiffMat:',sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1)
    print('sqDistances:',sqDistances)
    distances = sqDistances**0.5
    print(distances)
    sortedDistIndicies = distances.argsort()
    print(sortedDistIndicies)
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        print(voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        print('classCount',classCount)
    print('items:',classCount.items())
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedClassCount)
    return sortedClassCount[0][0]

# group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
# labels = ['A','A','B','B']
# print(classify0([0,0],group,labels,3))

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    print('returnMat:',returnMat)
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

import matplotlib
datingDataMat, datingLabel = file2matrix('datingTestSet2.txt')

from matplotlib import pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
plt.show()