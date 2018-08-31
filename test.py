#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

import pandas as pd
import numpy as np


def test1():
  data1 = np.array([[1,2.0,"3"], [4,5,6]] )
  index1 = ['a','b']
  columns1 = ['A','B','C']
  df = pd.DataFrame(data=data1, index = index1, columns = columns1)
  print df.dtypes
  print df

def test2():
  """
  1. data 有 行索引，有 列索引, 默认填充Nan
  2. dataframe 列名获取和判断
  """
  data3 = { 'A' : { 'a':1, 'b':4}, 'B': {'a':2,'b':5}, 'C':{'a':3, 'c':6} }
  df = pd.DataFrame(data=data3)
  print 'B' in list(df.columns)
  print 'M' in list(df.columns)
  print df

if __name__ == '__main__':
  test2()