#!/usr/bin/env python3

from random import sample, randint

# return list of common elements between two random lists of up to 50 numbers between 1 and 50 
print([ num for num in sample(range(50),randint(1,50)) if num in sample(range(50),randint(1,50)) ])

