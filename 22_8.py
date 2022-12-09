# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:00:05 2022

@author: Ian.lowther
"""

import numpy as np

#infile = "./inputs/8a_example.txt"
infile = "./inputs/8a.txt"

with open(infile,"r") as f:
  lines = f.read()
lines = lines.splitlines()
width = len(lines[0])
depth = len(lines)
height = np.zeros([depth,width])
for d in np.arange(depth):
  for w in np.arange(width):
    height[d,w] = lines[d][w]
visible = np.ones([depth,width])
scenic = np.zeros([depth,width])
for d in np.arange(1,depth-1):
  for w in np.arange(1,width-1):
    top_hidden = (height[d,w] <= height[:d,w]).any()
    left_hidden = (height[d,w] <= height[d,:w]).any()
    bot_hidden = (height[d,w] <= height[d+1:,w]).any()
    right_hidden = (height[d,w] <= height[d,w+1:]).any()
    visible[d,w] = 1 - (top_hidden * left_hidden * bot_hidden * right_hidden)
    
    top_view = 1; left_view = 1; bot_view = 1; right_view = 1
    while 1:
      if d-top_view-1 < 0:
        break
      if height[d,w] <= height[d-top_view,w]:
        break
      top_view += 1
    while 1:
      if w - left_view - 1 < 0:
        break
      if height[d,w] <= height[d,w-left_view]:
        break
      left_view += 1
    while 1:
      if d + bot_view + 1 >= depth:
        break
      if height[d,w] <= height[d+bot_view,w]:
        break
      bot_view += 1
    while 1:
      if w + right_view + 1 >= width:
        break
      if height[d,w] <= height[d,w+right_view]:
        break
      right_view += 1
    scenic[d,w] = top_view * left_view * bot_view * right_view
    
print("Solution 1: {}".format(np.sum(visible)))
print("Solution 2: {}".format(np.max(scenic)))