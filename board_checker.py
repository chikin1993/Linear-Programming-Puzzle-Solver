# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:50:18 2020

@author: Daniel Catlin

A function to check if a given configuration of pieces in the bug game is valid
"""

import numpy as np


def board_checker(piece_1, piece_2, piece_3, piece_4, piece_5,
                  piece_6, piece_7, piece_8, piece_9):

    # Combine the row vectors to form a matrix
    matrix = np.stack([piece_1, piece_2, piece_3, piece_4, piece_5,
                       piece_6, piece_7, piece_8, piece_9])

    # Extract the values from the matrix that are matching pairs
    pair_1 = matrix[0][1] + matrix[1][3]
    pair_2 = matrix[1][1] + matrix[2][3]
    pair_3 = matrix[3][1] + matrix[4][3]
    pair_4 = matrix[4][1] + matrix[5][3]
    pair_5 = matrix[6][1] + matrix[7][3]
    pair_6 = matrix[7][1] + matrix[8][3]
    pair_7 = matrix[0][2] + matrix[3][0]
    pair_8 = matrix[3][2] + matrix[6][0]
    pair_9 = matrix[1][2] + matrix[4][0]
    pair_10 = matrix[4][2] + matrix[7][0]
    pair_11 = matrix[2][2] + matrix[5][0]
    pair_12 = matrix[5][2] + matrix[8][0]

    # Check what pairs match and give true if all are 0
    if pair_1 == 0:
        if pair_2 == 0:
            if pair_3 == 0:
                if pair_4 == 0:
                    if pair_5 == 0:
                        if pair_6 == 0:
                            if pair_7 == 0:
                                if pair_8 == 0:
                                    if pair_9 == 0:
                                        if pair_10 == 0:
                                            if pair_11 == 0:
                                                if pair_12 == 0:
                                                    return True

    # Otherwise return false
    return False

# Testing
# piece_1 = np.array([-1,-3, 4, 2])
# piece_2 = np.array([-2, -1, 3, 2])
# pieces = [piece_1, piece_2]
# test = board_checker(pieces)
