# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""


import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    # Bruno's additionally defined test cases:

    def test_isosceles_A(self):
        self.assertEqual(classifyTriangle(40, 40, 60), 'Isosceles', '40, 40, 60 should be isosceles')

    def test_isosceles_B(self):
        self.assertEqual(classifyTriangle(2, 7, 7), 'Isosceles', '2, 7, 7 should be isosceles')

    def test_scalene_A(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '1, 2, 3 should be scalene')

    def test_scalene_B(self):
        self.assertEqual(classifyTriangle(100, 99, 102), 'Scalene', '100, 99, 102 should be scalene')

    def test_equilateral_C(self):
        self.assertEqual(classifyTriangle(0.1, 0.1, 0.1), 'InvalidInput', '0.1, 0.1, 0.1 has non-integer sides, making the input invalid')

    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1, 2, 3 does not satisfy the triangle inequality theorem and therefore is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

