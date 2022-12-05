# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:33:54 2022

@author: Ian
"""

import numpy as np

data_list = []
result_list = []
result_list_2 = []
with open("./inputs/4a.txt","r") as f:
  line_ndx = 0
  line = f.readline()
  while len(line) > 0:
    dash1 = line.find("-")
    comma = line.find(",")
    dash2 = line.find("-",comma)
    s1 = int(line[0:dash1])
    e1 = int(line[dash1+1:comma])
    s2 = int(line[comma+1:dash2])
    e2 = int(line[dash2+1:])
    data_list.append([s1,e1,s2,e2])
    if s1 >= s2 and e1 <= e2:
      result_list.append(line_ndx)
    elif s1 <= s2 and e1 >= e2:
      result_list.append(line_ndx)
    if e1 < s2:
      result_list_2.append(line_ndx)
    elif e2 < s1:
      result_list_2.append(line_ndx)
    line = f.readline()
    line_ndx += 1
data_list = np.array(data_list)

print("Solution 1: {}".format(len(result_list)))
print("Solution 2: {}".format(len(result_list_2)))
