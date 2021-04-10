# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:28:15 2020

@author: Daniel Catlin

Script to work on to solve that bug puzzle.

This is complete and should give a solution but is too slow to be feasible.

Here we assign the types of pieces numerical values such that a correct
pairing sums to 0

Cricket Head = +1
Cricket Tail = -1
Grub Head = +2
Grub Tail = -2
Ladybird Head = +3
Ladybird Tail = -3
Spider Head = +4
Spider Tail = -4
"""

# Bring in numpy for all the matrix operations
import numpy as np
from game_solver import game_solver

# Encode the pieces as vectors
piece_1 = np.array([-1, -3, 4, 2])
piece_2 = np.array([-2, -1, 3, 2])
piece_3 = np.array([-4, 2, 4, -1])
piece_4 = np.array([-3, -1, -4, -2])
piece_5 = np.array([-1, 2, 4, -3])
piece_6 = np.array([1, 3, -4, -2])
piece_7 = np.array([4, 3, -1, 2])
piece_8 = np.array([3, -3, 1, 4])
piece_9 = np.array([2, -4, 3, 1])

# Output of the game_solver
result = game_solver(piece_1, piece_2, piece_3, piece_4, piece_5,
                     piece_6, piece_7, piece_8, piece_9)

# Print them just incase
print(result)
