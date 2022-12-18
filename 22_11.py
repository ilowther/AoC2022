# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:25:35 2022

@author: Ian
"""
import numpy as np

class monkey:
  def __init__(self,starting_items,div,true,false):
    self.items = starting_items
    self.div = div
    self.true = true
    self.false = false
    self.inspect_count = 0

class m0(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old*3
  
class m1(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old*17
  
class m2(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old+1
  
class m3(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old+2
  
class m4(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old*old
  
class m5(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old+8

class m6(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old+6
  
class m7(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old+7
  
N_mon = 8
mon = {0: m0([93,54,69,66,71],7,7,1),
       1: m1([89,51,80,66],19,5,7),
       2: m2([90,92,63,91,96,63,64],13,4,3),
       3: m3([65,77],3,4,6),
       4: m4([76,68,94],2,0,6),
       5: m5([86,65,66,97,73,83],11,2,3),
       6: m6([78],17,0,1),
       7: m7([89,57,59,61,87,55,55,88],5,2,5)
      }

lcm = 1
for n in range(N_mon):
  lcm *= mon[n].div

for m in range(10000):
  for n in range(len(mon)):
    mon[n].inspect_count += len(mon[n].items)
    while len(mon[n].items) > 0:
      new = mon[n].op(mon[n].items[0])%lcm
#      new =int(np.floor(mon[n].op(mon[n].items[0])/3))
      if new%mon[n].div == 0:
        mon[mon[n].true].items.append(new)
      else:
        mon[mon[n].false].items.append(new)
      mon[n].items.pop(0)

unsorted_counts = [mon[n].inspect_count for n in range(N_mon)]
inspect_counts = np.sort([mon[n].inspect_count for n in range(len(mon))])
print("Solution: {}".format(int(inspect_counts[-1])*int(inspect_counts[-2])))

