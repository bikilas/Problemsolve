#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    # The element to be inserted
    value_to_insert = arr[-1]
    
    # Start from the second last element and move towards the start
    i = n - 2
    
    while (i >= 0) and (arr[i] > value_to_insert):
        arr[i + 1] = arr[i]  # Shift the element to the right
        print(" ".join(map(str, arr)))  # Print the array after each shift
        i -= 1
    
    # Insert the value in its correct position
    arr[i + 1] = value_to_insert
    print(" ".join(map(str, arr)))  # Print the final array

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
