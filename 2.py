def sort(arr):
    l = 0
    r = len(arr) - 1
    while r >= 0:
        m = [arr[l], l]
        while l <= r:
            m = max(m, [arr[l], l])
            l += 1
        l = 0
        arr[r], arr[m[1]] = arr[m[1]], arr[r]
        r -= 1
    return arr
