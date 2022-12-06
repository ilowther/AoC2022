# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 22:58:13 2022

@author: Ian
"""
import numpy as np

#infile = "./inputs/6a_example.txt"
#N_len = 4

infile = "./inputs/6a.txt"
N_len = 14

ndx = []
with open(infile,"r") as f:
  line = f.readline()
  while len(line) > 0:
    for n in range(N_len-1,len(line)):
      if len(np.unique([line[n-m] for m in range(N_len)])) < N_len:
        continue
      else:
        ndx.append(n+1)
        break
    line = f.readline()