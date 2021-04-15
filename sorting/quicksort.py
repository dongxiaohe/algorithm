def quicksort(arr):
    def _partition(arr, start, end):
        pivot = start
        for i in range(start + 1, end + 1):
            if arr[i] <= arr[start]:
                pivot += 1
                arr[i], arr[pivot] = arr[pivot], arr[i]
        arr[start], arr[pivot] = arr[pivot], arr[start] 
        return pivot
    def _quicksort(arr, start, end):
        if start < end:
            pivot = _partition(arr, start, end)
            _quicksort(arr, start, pivot - 1)
            _quicksort(arr, pivot + 1, end)
    _quicksort(arr, 0, len(arr) - 1)

arr = [7,2,3,7,2,3,4,12,1,3,4,4,2,2,1,1,2,30,15,17,13,23,27]
quicksort(arr)

assert(arr == sorted(arr))

