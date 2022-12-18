# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:28:37 2022

@author: Ian
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:25:35 2022

@author: Ian
"""
import numpy as np
#import warnings
#warnings.filterwarnings("ignore")

class monkey:
  def __init__(self,starting_items,div,true,false):
    self.items = starting_items
    self.div = div
    self.true = true
    self.false = false
    self.inspect_count = 0#np.uint64(0)


class ex0(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old*19
  

class ex1(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old+6

class ex2(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old*old
  
class ex3(monkey):
  def __init__(self,starting_items,div,true,false):
    monkey.__init__(self,starting_items,div,true,false)
  def op(self,old):
    return old+3

#ex = {0: ex0([np.ubyte(79),np.ubyte(98)],23, 2,3),
#      1: ex1([np.ubyte(54),np.ubyte(65),np.ubyte(75),np.ubyte(74)],19,2,0),
#      2: ex2([np.ubyte(79),np.ubyte(60),np.ubyte(97)],13,1,3),
#      3: ex3([np.ubyte(74)],17,0,1)}
    
ex = {0: ex0([79,98],23, 2,3),
      1: ex1([54,65,75,74],19,2,0),
      2: ex2([79,60,97],13,1,3),
      3: ex3([74],17,0,1)}

#lcm = np.lcm.reduce([23,19,13,17])
#lcm = 23*19*13*17
lcm = 1
for n in range(len(ex)):
  lcm *= ex[n].div

#for m in range(20):
#  for n in range(len(ex)):
    

for m in range(10000):
#  if m%20 == 0:
#    print(m)
  for n in range(len(ex)):
#    print("Monkey {}".format(n))
    ex[n].inspect_count += len(ex[n].items)
    while len(ex[n].items) > 0:
#      print("\tInspecting item value: {}".format(ex[n].items[0]))
      new = ex[n].op(ex[n].items[0])%lcm

#      new =int(np.floor(ex[n].op(ex[n].items[0])/3))
#      print("\t\tNew level is: {}".format(new))
      if new%ex[n].div == 0:
#        print("\tThis is divisible by {}".format(ex[n].div))
        ex[ex[n].true].items.append(new)
#        while new%lcm == 0:
#          new = new/lcm
#          print("It happened!")
#        print("\tItem was thrown to ex{}".format(ex[n].true))
      else:
#        print("\tThis is not divisible by {}".format(ex[n].div))
        ex[ex[n].false].items.append(new)
#        print("\tItem was thrown to ex{}".format(ex[n].false))
#      ex[n].inspect_count += 1
      ex[n].items.pop(0)

unsorted_counts = [ex[n].inspect_count for n in range(len(ex))]
inspect_counts = np.sort([ex[n].inspect_count for n in range(len(ex))])
print("Solution 1: {}".format(int(inspect_counts[-1])*int(inspect_counts[-2])))
