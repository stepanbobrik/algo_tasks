def sort(arr):
    swapped = 1
    while swapped:
        swapped = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = 1
    return arr


