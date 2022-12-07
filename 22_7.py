# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:39:44 2022

@author: Ian
"""

import numpy as np

#infile = "./inputs/7a_example.txt"
infile = "./inputs/7a.txt"

class folder:
  ctype = "folder"
  def __init__(self,name,parent):
    self.name = name
    self.parent = parent
    self.children = {}
    self.size = 0
  def add_size(self,s):
    self.size += s
    if self.name != "root":
      self.parent.add_size(s)
    
class file:
  ctype = "file"
  def __init__(self,name,size):
    self.name = name
    self.size = size
  
root = folder("root",0)

with open(infile,"r") as f:
  
  line = f.readline()
  while len(line) > 0:
    
    ls = line.split()
    if ls[0] == "$":
      if ls[1] == "cd":
        if ls[2] == '/':
          cur = root
        elif ls[2] == "..":
          cur = cur.parent
        else:
          cur = cur.children[ls[2]]
        line = f.readline()
          
      if ls[1] == "ls":
        line = f.readline()
        ls = line.split()
        if len(line) == 0:
          break
        while ls[0] != "$":
          if ls[0] == "dir":
            cur.children[ls[1]] = folder(ls[1],cur)
          else:
            cur.children[ls[1]] = file(ls[1],int(ls[0]))
            cur.add_size(int(ls[0]))
          line = f.readline()
          ls = line.split()
          if len(line) == 0:
            break

#%%
total_filespace = 70000000
update_size = 30000000
available_filespace = total_filespace - root.size
minimum_to_delete = update_size - available_filespace
folder_list = []
size_list= []
size_list_2 = []
def get_sizes(f_in):
  for key in f_in.children:
    if f_in.children[key].ctype == "folder":
      if f_in.children[key].size < 100000:
        folder_list.append(key)
        size_list.append(f_in.children[key].size)
      if f_in.children[key].size  > minimum_to_delete:
        size_list_2.append(f_in.children[key].size)
      get_sizes(f_in.children[key])
          
get_sizes(root)

print("Solution 1: {}".format(np.sum(size_list)))
print("Solution 2: {}".format(np.min(size_list_2)))

