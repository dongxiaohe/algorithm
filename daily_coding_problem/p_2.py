#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def process(arr):
    n = len(arr)
    result = [1 for _ in range(n)]
    for i in range(1, n):
        result[i] *= result[i - 1] * arr[i - 1]
    tmp = 1
    for i in range(n - 1, -1, -1):
        result[i] *= tmp
        tmp *= arr[i]
    return result

assert(process([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
assert(process([3, 2, 1]) == [2, 3, 6])
