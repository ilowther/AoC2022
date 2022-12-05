# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:01:17 2022

@author: Ian
"""

import numpy as np

#infile = "./inputs/5a_example.txt"
#N = 3

infile = "./inputs/5a.txt"
N = 9

part = 2

strings = ["" for n in np.arange(N)]
moves = []
with open(infile,"r") as f:
  line = f.readline()
  while len(line) > 0:
    if  "[" in line:
      for n in np.arange(N):
        if line[4*n+1] != " ":
          strings[n] += line[4*n+1]
          
    if line[0] == "m":
      space1 = line.find(" ")
      space2 = line.find(" ",space1+1)
      space3 = line.find(" ",space2+1)
      space4 = line.find(" ",space3+1)
      space5 = line.find(" ",space4+1)
      moves.append([int(line[space1+1:space2]),int(line[space3+1:space4])-1,int(line[space5:])-1])
      
    line = f.readline()
moves = np.array(moves)
for n in np.arange(len(moves)):
  x = moves[n,0]
  fr = moves[n,1]
  to = moves[n,2]
  if part == 1:
    strings[to] =  strings[fr][:x][::-1] + strings[to]
  elif part == 2:
    strings[to] =  strings[fr][:x] + strings[to]
    
  strings[fr] = strings[fr][x:]

result = ''
for n in np.arange(N):
  result += strings[n][0]
  

print("Solution: " + result)