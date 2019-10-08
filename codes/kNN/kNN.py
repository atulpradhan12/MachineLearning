from numpy import *
import operator

"""
Python also has the ability to return multiple values from a function call ,
something missing from many other languages. In this case the return values should
be a comma-separated list of values and Python then constructs a tuple and returns
this to the  caller
"""


def create_dataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def file2matrix(filename):
    fr = open(filename)  # opening a file
    arrayInLines = fr.readlines()  # reading no. of lines
    numberOfLines = len(arrayInLines)
    returnMat = zeros((numberOfLines, 3))  # return a new array of given shape and type, filled with zeros.
    classLabelVector = []
    index = 0
    for line in arrayInLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]  # List slice in Action
        classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat, classLabelVector


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # number of rows
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDisIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDisIndices[i]]
        classCount[votelabel] = classCount.get(votelabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
