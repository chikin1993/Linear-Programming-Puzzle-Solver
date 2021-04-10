# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:22:30 2020

@author: Daniel Catlin

A function to take the 9 pieces and test every permutation of them with roation_checker

This currently takes too long to find a solution but some improvements that might help could be:
    
    I think I can reduce the search set by 75% because the set of all possible options forms
    a set of 4 Equivalence classes and I can just search over one
    
        Create a function to find the 3 equivilence classes and throw them away before we start checking?
    
    It might also help to break the problem up in to 9 seperate peices that can be solved quicker
    to get a True or False and work through those
"""

import itertools
from constraint_checker import constraint_checker

def game_solver(piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7, piece_8, piece_9):
    
    # Create a list of all permutation of the pieces
    perm_list = list(itertools.permutations([piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7, piece_8, piece_9]))
    
    # Check every possible rotational arrangement for each permutation
    for i in range(len(perm_list)):  
        
        print("Checking tile configuration {} of {}".format(i, len(perm_list)))
        
        result = constraint_checker(perm_list[i][0], perm_list[i][1], perm_list[i][2], 
                                  perm_list[i][3], perm_list[i][4], perm_list[i][5], 
                                  perm_list[i][6], perm_list[i][7], perm_list[i][8])        
        
        if len(result) != 0:
            return result