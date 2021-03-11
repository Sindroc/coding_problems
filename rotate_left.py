#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:47:38 2021

@author: sindy
"""




def left_rotate(original_matrix):
    length = len(original_matrix)
    left_rotate =  [None]*length
    for row in range(length):                    # initialize the rotate matrix
        left_rotate[row] = [None] * length       # with None values        
    for row in range(length):
        for col in range(length):                # fill the matrix 
            left_rotate[row][col] = original_matrix[col][length - row - 1]
    return left_rotate


original_matrix = [[1,2,3], [4,5,6], [7,8,9]]
left_rotate(original_matrix)
