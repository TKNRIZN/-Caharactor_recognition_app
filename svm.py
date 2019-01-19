#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:05:24 2018

@author: takanori
"""
import numpy as np
from sklearn import svm
from sklearn.externals import joblib


train_data = np.loadtxt('./data/train_data.csv',delimiter=',',dtype=float)
train_label = np.loadtxt('./data/train_label.csv',delimiter=',',dtype=float)
test_data =np.loadtxt('./data/testdata.csv',delimiter=',',dtype=float)



clf = svm.SVC(kernel='rbf', C=10, gamma=0.1)
clf.fit(train_data,train_label);

#save model
joblib.dump(clf, './clf.pkl') 