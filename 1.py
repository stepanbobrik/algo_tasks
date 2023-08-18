def sort(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            arr[i],arr[i-1] = arr[i-1],arr[i]
