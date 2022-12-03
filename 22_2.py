# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:50:00 2022

@author: Ian
"""

import numpy as np

def rps(opp, me):
  win = 6
  draw = 3
  loss = 0
  rock = 1
  paper = 2
  scissors = 3
  if opp == "A": # Rock
    if me == "X": # Rock
      return rock + draw
    elif me == "Y": # Paper
      return paper + win
    elif me == "Z": # Scissors
      return scissors + loss
  elif opp == "B": # Paper
    if me == "X": # Rock
      return rock + loss
    elif me == "Y": # Paper
      return paper + draw
    elif me == "Z": # Scissors
      return scissors + win
  elif opp == "C": # Scissors
    if me == "X": # Rock
      return rock + win
    elif me == "Y": # Paper
      return paper + loss
    elif me == "Z": # Scissors
      return scissors + draw
  else:
    return np.nan

guide = np.loadtxt("./inputs/2a.txt",dtype = str)
N_games = np.size(guide,0)

guide_results = np.array([rps(guide[n,0],guide[n,1]) for n in np.arange(N_games)])
print("Solution 1: {}".format(np.sum(guide_results)))

def rps2(opp,me):
  win = 6
  draw = 3
  loss = 0
  rock = 1
  paper = 2
  scissors = 3
  if opp == "A": # Rock
    if me == "X": # Lose
      return loss + scissors
    elif me == "Y": # Draw
      return draw + rock
    elif me == "Z": # Win
      return win + paper
  elif opp == "B": # Paper
    if me == "X": # Lose
      return loss + rock
    elif me == "Y": # Draw
      return draw + paper
    elif me == "Z": # Win
      return win + scissors
  elif opp == "C": # Scissors
    if me == "X": # Lose
      return loss + paper
    elif me == "Y": # Draw
      return draw + scissors
    elif me == "Z": # Win
      return win + rock
  else:
    return np.nan
  
guide_results2 = np.array([rps2(guide[n,0],guide[n,1]) for n in np.arange(N_games)])
print("Solution 2: {}".format(np.sum(guide_results2)))
  