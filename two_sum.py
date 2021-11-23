def twoSum(nums, target):
    nums.sort()
    ans = []
    l, r = 0, len(nums) - 1
    while l < r:
        sum = nums[l] + nums[r]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            ans.append([nums[l], nums[r]])
            l += 1
            r -= 1
    return ans