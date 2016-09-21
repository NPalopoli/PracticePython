#!/usr/bin/env python3

num = int(input("Please enter a number: "))
check = int(input("Please enter a number to divide by: "))

def divideEvenly(num,check):
  if num % check == 0:
    return True
  else:
    return False
  
if divideEvenly(num,2):
  if divideEvenly(num,4):
    odd_or_even = "even and multiple of 4"
  else:
    odd_or_even = "even"
else:
  odd_or_even = "odd"

if divideEvenly(num,check):
  odd_or_even = odd_or_even + ". It divides evenly into " + str(check)
else:
  odd_or_even = odd_or_even + ". It does not divide evenly into " + str(check)

print("The number is " + odd_or_even + ".")
