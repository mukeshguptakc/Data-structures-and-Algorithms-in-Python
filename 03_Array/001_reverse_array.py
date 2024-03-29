import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    for i in range(0,len(a)//2):
        temp = a[i]
        a[i] = a[(len(a)-1)-i]
        a[(len(a)-1)-i] = temp
    return a

if __name__ == '__main__':
    
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print("Prior to Reverse: arr_count: {} arr: {}".format(arr_count, arr))
    res = reverseArray(arr)
    print("Post Reverse: arr_count: {} arr: {}".format(arr_count, arr))


"""
python 001_reverse_array.py
6
6 5 4 3 2 1
Prior to Reverse: arr_count: 6 arr: [6, 5, 4, 3, 2, 1]
Post Reverse: arr_count: 6 arr: [1, 2, 3, 4, 5, 6]
"""