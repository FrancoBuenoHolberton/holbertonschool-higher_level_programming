#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    resto = number % 10
else:
    resto = (-1 * (-number % 10))
    restoneg = 0
if resto != 0:
    restoneg = "less than 6 and not 0"
if resto > 5:
    restoneg = "greather than 5"
print("Last digit of {} is {} is {}".format(number, resto, restoneg))
