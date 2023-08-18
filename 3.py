def sort(nums):
    def insert(arr, el):
        r = len(arr) - 1
        while arr[r] > el:
            r -= 1
        r += 1
        arr.insert(r, el)

    ans = []
    for n in nums:
        if not ans:
            ans.append(n)
        else:
            insert(ans, n)
    return ans
