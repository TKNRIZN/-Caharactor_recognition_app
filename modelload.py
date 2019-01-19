#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:36:07 2018

@author: takanori
"""

from sklearn import datasets
from sklearn.externals import joblib
import numpy as np

test_data =np.loadtxt('./data/testdata.csv',delimiter=',',dtype=float)


# 予測モデルを復元
clf = joblib.load('./clf.pkl') 


# 予測結果を出力
print(clf.predict([test_data]))