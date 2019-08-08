#!/bin/python3
# Day 3: Intro to Conditional Statements
# https://www.hackerrank.com/challenges/30-conditional-statements/problem

import math
import os
import random
import re
import sys

"""
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
"""

if __name__ == '__main__':
    N = int(input())

if( N%2==1) or (N>5 and N<21):
    print("Weird")
else:
    print("Not Weird")

    
