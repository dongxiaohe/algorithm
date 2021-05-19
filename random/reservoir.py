import random
def reservoir(arr):
    k = 1
    chosen = -1
    for i in range(len(arr)):
        index = random.randint(0, k - 1)
        k += 1
        if index == 0:
            chosen = i
    return chosen

arr = list(range(5))
for _ in arr:
    print(arr[reservoir(arr)])

