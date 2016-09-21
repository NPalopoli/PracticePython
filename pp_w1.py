#!/usr/bin/env python3

import datetime

name = input("Please enter your name: ")
age = input("Please enter your age: ")

year = datetime.date.today().year
hundred_years = str(year + 100 - int(age))

print("Greetings, " + name + ". You will be 100 years old in " + hundred_years + ".")


