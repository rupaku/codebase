#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'theFinalProblem' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING target as parameter.
# import pdb
def flipbits(x):
    return 1 if (x == 0) else 0


def theFinalProblem(target):
    # Write your code here

    length = len(target)
    res=[]
    initiallist=[]
    res = [0] * length
    print(res)
    for i in target:
        initiallist.append(int(i))
    print(initiallist)
    count = 0
    flag = False
    for j in range(length):
        if initiallist[j] != res[j]:
            print(initiallist[j],res[j])
            temp = j
            while temp < length:
                res[temp] = flipbits(res[temp])
                temp = temp + 1
                flag = True
            if flag:
                count = count + 1
                flag = False

    return count


if __name__ == '__main__':
    # pdb.set_trace()
    target = '0011'

    result = theFinalProblem(target)
    print(result)