def sort(nums):
    not_sorted = 1
    while not_sorted:
        not_sorted = 0
        to_insert = nums.pop()
        for i in range(len(nums)):
            if nums[i] > to_insert:
                nums.insert(i, to_insert)
                not_sorted = 1
                break
            if i == len(nums)-1:
                i+=1
                nums.insert(i, to_insert)
                return nums
    return nums
