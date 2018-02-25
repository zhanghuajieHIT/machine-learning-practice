# -*- coding: utf-8 -*-
# @Author: zhanghuajieHIT
# @Date:   2018-02-25 14:30:47
# @Last Modified by:   zhanghuajieHIT
# @Last Modified time: 2018-02-25 14:58:29

from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistance =sqDiffMat.sum(axis = 1)
	distances = sqDistance ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

if __name__ == "__main__":
	group, labels = createDataSet()
	result = classify([0, 0], group, labels, 3)
	print (result)
