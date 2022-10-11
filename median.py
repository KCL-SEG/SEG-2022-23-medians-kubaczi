"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if not len(numbers)%2==0:
            medianno=math.floor(len(numbers)/2)
            median=numbers[medianno]
        else:
            medianno=math.floor(len(numbers)/2)
            median=(numbers[medianno-1]+numbers[medianno])/2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
