#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:37:00 2021

@author: sindy
"""


def three_quarter_rotate(original_matrix):
    length = len(original_matrix)
    three_quarter_rotate =  [None]*length
    for row in range(length):                    # initialize the rotate matrix
        three_quarter_rotate[row] = [None] * length       # with None values        
    for row in range(length):
        for col in range(length):                # fill the matrix 
            three_quarter_rotate[row][col] = original_matrix[length - col -1][row]
            print(three_quarter_rotate)
    return three_quarter_rotate


original_matrix = [[1,2,3], [4,5,6], [7,8,9]]
three_quarter_rotate(original_matrix)



