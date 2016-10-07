#!/usr/bin/env python3

num = int(input("Please enter a number: "))

def divideEvenly(num,check):
  if num % check == 0:
    return True
  else:
    return False
  
print("%s is dividable by %s" % (num, num), end="")
for divisor in range(num-1,0,-1):
  if divideEvenly(num,divisor):
    if divisor==1:
      print(" and %s." % divisor)
    else:
      print(", %s" % divisor, end="")

