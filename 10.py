def maxSum(nums):
    sum = 0
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        sum+=n
        max_sum = max(max_sum,sum-min_sum)
        min_sum =min(sum,min_sum)
    return max_sum