# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:52:19 2022

@author: Ian
"""
import numpy as np

with open("./inputs/3a.txt","r") as f:
#with open("./inputs/3a_Example.txt","r") as f:
  line = f.readline()
  total = 0
  tuplist = []
  priority_list = []
  line_no = 0
  while len(line)>0:
    L = len(line)-1
    left = line[0:int(L/2)]
    right = line[int(L/2):]
    for n in np.arange(len(left)):
      if right.find(left[n]) >= 0:
        if left[n].islower():
          tuplist.append([line_no,left[n],ord(left[n])-96])
          priority_list.append(ord(left[n])-96)
          total += ord(left[n])-96
        else:
          tuplist.append([line_no,left[n],ord(left[n])-38])
          priority_list.append(ord(left[n])-38)
          total += ord(left[n])-38
        break
    line = f.readline()
    line_no += 1
print("Solution 1: {}".format(np.sum(total)))

with open("./inputs/3a.txt","r") as f:
#with open("./inputs/3b_example.txt","r") as f:
  e1 = f.readline()
  e2 = f.readline()
  e3 = f.readline()
  badge_list = []
  badge_priority_list = []
  while len(e1) > 0:
    for n in np.arange(len(e1)):
      if e2.find(e1[n]) >= 0 and e3.find(e1[n]) >= 0:
        badge_list.append(e1[n])
        if e1[n].islower():
          badge_priority_list.append(ord(e1[n])-96)
        else:
          badge_priority_list.append(ord(e1[n])-38)
        break
    e1 = f.readline()
    e2 = f.readline()
    e3 = f.readline()
print("Solution 2: {}".format(np.sum(badge_priority_list)))
