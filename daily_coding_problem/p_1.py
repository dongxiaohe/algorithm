# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def twoSum(arr, target):
    kv = {}
    for i in range(len(arr)):
        if target - arr[i] in kv:
            return True
        kv[arr[i]] = True
    return False

print(twoSum([10, 15, 3, 7], 17))
print(twoSum([10, 15, 3, 7], 30))

