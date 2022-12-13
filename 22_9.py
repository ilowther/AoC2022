# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:58:40 2022

@author: Ian
"""

import numpy as np

#infile = "./inputs/9a_example.txt"
infile = "./inputs/9a.txt"

with open(infile,"r") as f:
  lines = f.read()
lines = lines.splitlines()
motion = np.array([lines[n].split() for n in np.arange(len(lines))])

H = np.array([0,0]) # row, col
T = np.array([0,0]) # row, col
T_visit = np.zeros([1000,1000])
T_visit[0,0] = 1
for m in np.arange(len(lines)):
  x = motion[m,0]
  for n in np.arange(int(motion[m,1])):
    if x == "R":
      H += np.array([0,1])
      if H[1] - T[1] > 1:
        T = np.array([H[0],H[1]-1])
        T_visit[T[0],T[1]] = 1
    elif x == "U":
      H += np.array([1,0])
      if H[0] - T[0] > 1:
        T = np.array([H[0]-1,H[1]])
        T_visit[T[0],T[1]] = 1
    elif x == "L":
      H += np.array([0,-1])
      if T[1] - H[1] > 1:
        T = np.array([H[0],H[1]+1])
        T_visit[T[0],T[1]] = 1
    elif x == "D":
      H += np.array([-1,0])
      if T[0] - H[0] > 1:
        T = np.array([H[0]+1,H[1]])
        T_visit[T[0],T[1]] = 1
    
print("Solution 1: {}".format(np.sum(T_visit)))

#infile2 = "./inputs/9b_example.txt"
infile2 = "./inputs/9a.txt"

with open(infile2,"r") as f:
  lines2 = f.read()
lines2 = lines2.splitlines()
motion2 = np.array([lines2[n].split() for n in np.arange(len(lines2))])
N_knots = 10
knots = {0:np.array([0,0]),
         1:np.array([0,0]),
         2:np.array([0,0]),
         3:np.array([0,0]),
         4:np.array([0,0]),
         5:np.array([0,0]),
         6:np.array([0,0]),
         7:np.array([0,0]),
         8:np.array([0,0]),
         9:np.array([0,0])}
T_visit2 = np.zeros([10000,10000])
T_visit2[0,0] = 1
    
for m in np.arange(len(lines2)):
  x = motion2[m,0]
  for n in np.arange(int(motion2[m,1])):
    if x == "R":
      knots[0][1] += 1
    elif x == "U":
      knots[0][0] += 1
    elif x == "L":
      knots[0][1] -= 1
    elif x == "D":
      knots[0][0] -= 1
    for k in np.arange(1,N_knots):
      if knots[k][0] != knots[k-1][0] and np.abs(knots[k][1] - knots[k-1][1]) > 1:
        knots[k][0] += np.sign(knots[k-1][0] - knots[k][0])
        knots[k][1] += np.sign(knots[k-1][1] - knots[k][1])
      if np.abs(knots[k][0] - knots[k-1][0]) > 1 and knots[k][1] != knots[k-1][1]:
        knots[k][0] += np.sign(knots[k-1][0] - knots[k][0])
        knots[k][1] += np.sign(knots[k-1][1] - knots[k][1])
      elif np.abs(knots[k][0]-knots[k-1][0]) > 1:
        knots[k][0] += np.sign(knots[k-1][0] - knots[k][0])
      elif np.abs(knots[k][1] - knots[k-1][1]) > 1:
        knots[k][1] += np.sign(knots[k-1][1] - knots[k][1])
    T_visit2[knots[9][0],knots[9][1]] = 1
      
print("Solution 2: {}".format(np.sum(T_visit2)))