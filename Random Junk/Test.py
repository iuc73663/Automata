# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:17:38 2018

@author: Kevin
"""

import numpy as np

np.random.seed(123)
# Create an 3 by 3 array of random numbers between 1 and 20
my_arr = np.random.randint(1, 20, size = (3, 3))
print(my_arr)
# Convert the array to a nested list
my_list = my_arr.tolist()

print(my_list)