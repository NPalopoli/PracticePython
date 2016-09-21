#!/usr/bin/env python3

import datetime

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
num = int(input("Please give me a number: "))

year = datetime.date.today().year
hundred_years = str(year + 100 - age)

print ( str("Greetings, " + name + ". You will be 100 years old in " + hundred_years + ".\n") * num, end="")


