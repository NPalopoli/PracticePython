#!/usr/bin/env python3

maxlimit = int(input("Please enter an integer to be used as maximum limit: "))  # ask the user for maximum limit
numlist = [ int(num) for num in input("Please enter a list of integers separated by spaces: ").split() if int(num) <= maxlimit ]  # create list of numbers below limit from user input
print("Your limited list of integers is: %s" % str(numlist))  # print limited list

