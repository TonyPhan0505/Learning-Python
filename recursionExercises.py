import sys
sys.setrecursionlimit(5000000)
def sum_of_harmonic_series(n):
	if n<2:
		return 1
	else:
		return (1/n) + (sum_of_harmonic_series(n-1))

def common_divisor(a,b):
	low = min(a,b)
	high = max(a,b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return common_divisor(low, high%low)

def sum_series_positives(n):
	if n < 1:
		return 0
	else:
		return n + sum_series_positives(n-2)

def factorial(n):
	if n<=1:
		return 1
	else: 
		n * factorial(n-1)

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

def kSum(nums, target, k):
    res = []
    
    # If we have run out of numbers to add, return res.
    if not nums:
        return res
    
    # There are k remaining values to add to the sum. The 
    # average of these values is at least target // k.
    average_value = target // k
    
    # We cannot obtain a sum of target if the smallest value
    # in nums is greater than target // k or if the largest 
    # value in nums is smaller than target // k.
    if average_value < nums[0] or nums[-1] < average_value:
        return res
    
    if k == 2:
        return twoSum(nums, target)

    for i in range(len(nums)):
        if i == 0 or nums[i - 1] != nums[i]:
            for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                res.append([nums[i]] + subset)

    return res

print(kSum([4,1,4,2,3], 8, 2))

def intToRoman(num):
    num = int(num)
    roman = ''
    d = {1:'I', 5:'V', 10:'X', 50:'L', 90:'XC', 100:'C', 500:'D', 900:'CM', 1000:'M'}
    ans = []
    def find(num, roman):
        if num in list(d.keys()):
            roman += d[num]
            ans.append(roman)
        elif 1<num<1000:
            for i in range(len(list(d.keys()))):
                if list(d.keys())[i] - num > 1:
                    roman += d[list(d.keys())[i-1]]
                    find(num-list(d.keys())[i-1], roman)
                elif list(d.keys())[i] - num == 1:
                    roman += 'I' + d[list(d.keys())[i]]
                    ans.append(roman)

        elif num > 1000:
            roman += d[1000]
            find(num-1000, roman)

        return num, roman
    if num < 1:
        roman += 'Invalid'
    else:
        find(num, roman)
    return ans[0]


