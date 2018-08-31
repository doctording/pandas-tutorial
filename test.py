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

def test3():
  """
  1. dataframe 查
  """
  data3 = { 'A' : { 'a':1, 'b':4}, 'B': {'a':2,'b':5}, 'C':{'a':3, 'c':6} }
  df = pd.DataFrame(data=data3)
  print df.values
  print df.columns
  # index + column 定位
  print df.at['a', 'B'] # 'a' index(行), 'B' column
  print df['A'] # 'A' column
  print df.loc[['b', 'c']] # 'b', 'c',index(行)
  print df.loc['b'].at['B'] # 'b' index(行),, 'B' column
  print "===="
  print df.iloc[0] # 第0行
  print df.iloc[0, 1] # 第0行,第1列


def test4():
  """
  1. dataframe alter
  """
  data3 = { 'A' : { 'a':1, 'b':4}, 'B': {'a':2,'b':5}, 'C':{'a':3, 'c':6} }
  df = pd.DataFrame(data=data3)
  df2 = df.copy() # 深度拷贝
  print df2
  df2['D'] = [1.0, 5, 7] # add 'D' column
  df2.pop('B')
  print df2
  df2.insert(1, 'bar', [ 1, 2, None]) # insert 'bar' column
  df2.insert(1, 'bar2', [ 1, None, 2])
  print df2
  df3 = df2.assign(E=lambda x: x['A'] + x['D'])
  print df3
 

if __name__ == '__main__':
  test4()
