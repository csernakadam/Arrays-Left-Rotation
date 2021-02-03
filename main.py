#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    # if the size of k > len(a), rotate only necessary with
    # module of the division
    rotations = d % len(a)
    print (rotations)
    return a[rotations:] + a[:rotations]


print ( rotLeft([1,2,3,4,5,6],2))