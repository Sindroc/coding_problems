#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:50:03 2021

@author: sindy
"""

import unittest
import rotate_right
import rotate_left
import rotate_half
import rotate_three_quart
   
class Test(unittest.TestCase): 
    
    def test_left(self):        
        matriz1 = [[1,2,3], [4,5,6],[7,8,9]]
        matriz2 = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
        self.assertEqual(rotate_left.left_rotate(matriz1), matriz2)


    def test_right(self):        
        matriz1 = [[1,2,3], [4,5,6],[7,8,9]]
        matriz2 = [[7,4,1], [8,5,2],[9,6,3]]
        self.assertEqual(rotate_right.right_rotate(matriz1), matriz2)
        
    def test_half(self):
        matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
        matriz2 = [[9,8,7],[6,5,4],[3,2,1]]
        self.assertEqual(rotate_half.half_rotate(matriz1), matriz2) 

    def test_three_quarter(self):
        matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
        matriz2 = [[7,4,1],[8,5,2], [9,6,3]]
        self.assertEqual(rotate_three_quart.three_quarter_rotate(matriz1), matriz2) 
               
            
if __name__ == "__main__":
    unittest.main()        
    
    
    