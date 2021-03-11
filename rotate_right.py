#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:28:20 2021
Given an image represented by an NxN matrix, where 
each pixel in the image is 4 bytes, write a method to 
rotate the image by 90 degrees. Can you do this in place?
@author: sindy
"""


def right_rotate(original_matrix):
    length = len(original_matrix)
    right_rotate = [None]*length
    for row in range(length):                    # initialize the rotate matrix
        right_rotate[row] = [None] * length            # with None values 
    for row in range(length):
        for col in range(length):                # fill the matrix 
            right_rotate[col][row] = original_matrix[length - row - 1][col]
    return right_rotate
    
    
    # A = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
original_matrix = [[1,2,3], [4,5,6], [7,8,9]]



right_rotate(original_matrix)

