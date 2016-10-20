# coding: utf-8

from __future__ import print_function

from numpy import *

######### the simple usage of numpy ########

a = arange(15).reshape(3, 5)
print(a)
print(a.shape, a.ndim, a.dtype.name, a.itemsize, a.size)

###### array division ###

a = array([2, 3, 4])
print(a.dtype)

A = array([[1, 1],
           [0, 1]])

B = array([[2, 0],
           [3, 4]])
print("A与B的数量和为: ")
print(A * B)

print ("\n")

print("A与B的向量和为: ")
print(dot(A, B))

