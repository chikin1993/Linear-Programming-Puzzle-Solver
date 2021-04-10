# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:48:02 2020

@author: Daniel Catlin

A function to take a list of 9 pieces and test every possible
rotational configuration for each
"""

import numpy as np
from board_checker import board_checker


def rotation_checker(piece_1, piece_2, piece_3, piece_4, piece_5,
                     piece_6, piece_7, piece_8, piece_9):

    # Loop through each rotation of all pieces sequentially checking if valid
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        for n in range(4):
                            for o in range(4):
                                for p in range(4):
                                    for q in range(4):
                                        result = board_checker(
                                               np.roll(piece_1, i),
                                               np.roll(piece_2, j),
                                               np.roll(piece_3, k),
                                               np.roll(piece_4, l),
                                               np.roll(piece_5, m),
                                               np.roll(piece_6, n),
                                               np.roll(piece_7, o),
                                               np.roll(piece_8, p),
                                               np.roll(piece_9, q))
                                        if result:
                                            return [i, j, k, l, m, n, o, p, q]

    return False
