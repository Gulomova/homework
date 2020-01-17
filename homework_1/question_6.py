# Question 6
from builtins import input, round, int, str
from math import *

C, H = 50, 30


def calc(D):
    return sqrt((2*C*D)/H)


D = input().split(',')
D = [int(i) for i in D]
D = [calc(i) for i in D]
D = [round(i) for i in D]
D = [str(i) for i in D]

print(",".join(D))

