# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:07:44 2022

@author: Ian
"""

import numpy as np

fname = "./inputs/1a.txt"

with open(fname,'rb') as f:
  fbytes = f.read()
  f.close()
  
start = 0
stop = 0
d_ndx = 0
d_list = []
elves = {}
#%%
while 1:
  stop = fbytes.find(b'\r',start)
  if stop < 0:
    break
  d_list.append(int(fbytes[start:stop]))
  if fbytes[stop+2:stop+4] == b'\r\n':
    elves[d_ndx] = d_list
    d_list = []
    d_ndx += 1
    start = stop+4
  else:
    start = stop+2
#%%
N_elves = len(elves)
total_cals = np.array([np.sum(elves[n]) for n in np.arange(N_elves)])
print("Solution 1: {}".format(np.max(total_cals)))

cals_sorted = np.sort(total_cals)
print("Solution 2: {}".format(cals_sorted[-3]+cals_sorted[-2]+cals_sorted[-1]))
