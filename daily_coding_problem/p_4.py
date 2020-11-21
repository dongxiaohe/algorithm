# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# 
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def findNumber(arr):
    m = len(arr)
    for i in range(m):
        while 0 < arr[i] <= m and arr[arr[i] - 1] != arr[i]: # Make sure right number in the right place
            k = arr[i] - 1 # multi assign won't work with nested variables
            arr[i], arr[k] = arr[k], arr[i]
    for i in range(m):
        if arr[i] != i + 1: return i + 1
    return m + 1

assert(findNumber([3, 4, -1, 1]) == 2)
assert(findNumber([1, 2, 0]) == 3)

