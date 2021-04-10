# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:36:51 2020

@author: Daniel Catlin

Function used to check every combination of positions for
one placement of the tiles
"""

import constraint
import numpy as np
import time


def constraint_checker(piece_1, piece_2, piece_3, piece_4, piece_5,
                       piece_6, piece_7, piece_8, piece_9, timing=False):

    # Find the start time if we want the execution time for this function
    if timing:
        start_time = time.time()

    # Create the set of rotations for each piece
    piece_1_set = [list(np.roll(piece_1, i)) for i in range(4)]
    piece_2_set = [list(np.roll(piece_2, i)) for i in range(4)]
    piece_3_set = [list(np.roll(piece_3, i)) for i in range(4)]
    piece_4_set = [list(np.roll(piece_4, i)) for i in range(4)]
    piece_5_set = [list(np.roll(piece_5, i)) for i in range(4)]
    piece_6_set = [list(np.roll(piece_6, i)) for i in range(4)]
    piece_7_set = [list(np.roll(piece_7, i)) for i in range(4)]
    piece_8_set = [list(np.roll(piece_8, i)) for i in range(4)]
    piece_9_set = [list(np.roll(piece_9, i)) for i in range(4)]

    # Initialise the constraint problem class
    problem = constraint.Problem()

    # Add the variables to the problem and their domain sets
    problem.addVariable("1", piece_1_set)
    problem.addVariable("2", piece_2_set)
    problem.addVariable("3", piece_3_set)
    problem.addVariable("4", piece_4_set)
    problem.addVariable("5", piece_5_set)
    problem.addVariable("6", piece_6_set)
    problem.addVariable("7", piece_7_set)
    problem.addVariable("8", piece_8_set)
    problem.addVariable("9", piece_9_set)

    # Add the constraints required to solve the puzzle
    problem.addConstraint(lambda i, j: i[1] + j[3] == 0, ("1", "2"))
    problem.addConstraint(lambda i, j: i[1] + j[3] == 0, ("4", "5"))
    problem.addConstraint(lambda i, j: i[1] + j[3] == 0, ("7", "8"))
    problem.addConstraint(lambda i, j: i[1] + j[3] == 0, ("2", "3"))
    problem.addConstraint(lambda i, j: i[1] + j[3] == 0, ("5", "6"))
    problem.addConstraint(lambda i, j: i[1] + j[3] == 0, ("8", "9"))
    problem.addConstraint(lambda i, j: i[2] + j[0] == 0, ("1", "4"))
    problem.addConstraint(lambda i, j: i[2] + j[0] == 0, ("4", "7"))
    problem.addConstraint(lambda i, j: i[2] + j[0] == 0, ("2", "5"))
    problem.addConstraint(lambda i, j: i[2] + j[0] == 0, ("5", "8"))
    problem.addConstraint(lambda i, j: i[2] + j[0] == 0, ("3", "6"))
    problem.addConstraint(lambda i, j: i[2] + j[0] == 0, ("6", "9"))

    # Give a list of all solutions
    solutions = problem.getSolutions()

    # Find end time and difference, return this with solutions
    if timing:
        end_time = time.time()
        execution_time = end_time - start_time
        return solutions, execution_time
    else:
        return solutions
