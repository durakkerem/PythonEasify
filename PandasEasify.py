# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 22:19:38 2017

@author: durak
"""


#def changeColumnName(df, oldName, newName, index): 
      
def deleteColumn(df, indexOrList):
      temp = ['Wrong type of indexOrList!']
      if (type(indexOrList) == list):
            temp = df.drop(df.columns[indexOrList], axis=1)
      elif (type(indexOrList) == int):
            temp = df.drop(df.columns[[indexOrList]], axis=1)
      
      return temp
      
#def addColumn(df, listOfRows, colName):
      
def findIndexThatContains(df, query):
      allIndexes = []
      for index, row in df.iterrows():
            columnIndex = 0
            rowIndex = 0
            if (str(query) in str(row)):
                  li = list(row)
                  rowIndex = index
                  for index, item in enumerate(li):
                        if(query in item):
                              columnIndex = index
                  allIndexes.append([rowIndex, fromRowColumnIndex(df, rowIndex, columnIndex)])
      return allIndexes

      
def fromRowColumnIndex(df, row, column):
      temp = df[[column]]
      return temp.loc[row].values[0]