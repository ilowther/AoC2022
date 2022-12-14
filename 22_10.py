# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:32:13 2022

@author: Ian
"""

import numpy as np

#infile = "./inputs/10a_example.txt"
#infile = "./inputs/10a_example2.txt"
infile = "./inputs/10a.txt"

with open(infile,"r") as f:
  lines = f.read().splitlines()


X = [1]
pixels = []
col = 0

# Start cycle n: Begin or continue execution
# Draw CRT pixel on col%40
# End of cycle n: update X
for line in lines:
  if line == "noop":
    if np.abs(col%40 - X[-1]) <= 1:
      pixels.append("#")
    else:
      pixels.append(".")
    col += 1
    X += [X[-1]]
  elif line.split()[0] == "addx":
    if np.abs(col%40 - X[-1]) <= 1:
      pixels.append("#")
    else:
      pixels.append(".")
    col += 1
    X += [X[-1]]
    if np.abs(col%40 - X[-1]) <= 1:
      pixels.append("#")
    else:
      pixels.append(".")
    col += 1
    X += [X[-1]+int(line.split()[1])]
    
N = int(np.floor((len(X) - 20)/40))+1
test_points = np.append([20],20+np.arange(1,N)*40)-1
test_values = np.array(X)[test_points]

print("Solution 1: {}".format(np.sum((test_points+1)*test_values)))

crt=np.reshape(pixels,[6,40])