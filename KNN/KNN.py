#!/usr/bin/env python2
# -*- coding:utf8 -*-
# @TIME   : 2/22/18 11:28 PM
# @Author : ZHJ
# @File   : KNN.py

from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]

