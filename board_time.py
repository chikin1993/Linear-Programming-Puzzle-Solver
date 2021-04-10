# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:34:02 2021

@author: DanielCatlin

Quick script to time execution of one run of board_checker
"""

from board_checker import board_checker
from timeit import timeit
import numpy as np


# Define a quick function to run the default values of the pieces
def time():
    piece_1 = np.array([-1, -3, 4, 2])
    piece_2 = np.array([-2, -1, 3, 2])
    piece_3 = np.array([-4, 2, 4, -1])
    piece_4 = np.array([-3, -1, -4, -2])
    piece_5 = np.array([-1, 2, 4, -3])
    piece_6 = np.array([1, 3, -4, -2])
    piece_7 = np.array([4, 3, -1, 2])
    piece_8 = np.array([3, -3, 1, 4])
    piece_9 = np.array([2, -4, 3, 1])
    board_checker(piece_1, piece_2, piece_3, piece_4, piece_5,
                  piece_6, piece_7, piece_8, piece_9)


sec = timeit(time)
