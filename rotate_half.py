#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:26:55 2021
rotate 180.
@author: sindy
"""

def half_rotate(original_matrix):
    length = len(original_matrix)
    half_rotate =  [None]*length
    for row in range(length):                    # initialize the rotate matrix
        half_rotate[row] = [None] * length       # with None values        
    for row in range(length):
        for col in range(length):                # fill the matrix 
            half_rotate[row][col] = original_matrix[length - row - 1][length - col - 1]
    return half_rotate


original_matrix = [[1,2,3], [4,5,6], [7,8,9]]
half_rotate(original_matrix)

