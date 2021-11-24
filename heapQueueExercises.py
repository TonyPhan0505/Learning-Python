import heapq as hq
from collections import defaultdict
from functools import reduce
from collections import Counter
import math

# Uses:
# find n largest/ smallest, most frequent/ least frequent



def isValidSoduku(board):
	seen = []
	for row in range(9):
		for col in range(9):
			val = board[row][col]
			if val == ".":
				continue
			if (val, row) in seen or (val, col) in seen or (val, row//3, col//3) in seen:
				return "Invalid"
			seen.append((val, row))
			seen.append((val, col))
			seen.append((val, row//3, col//3))

	return True

print(isValidSoduku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

def n_largest_smallest_nums(n,nums_lst):
	return hq.nlargest(n, nums_lst), hq.nsmallest(n,nums_lst)

def delete_smallest_insert_new(nums_lst, new):
	hq.heapreplace(nums_lst, new)
	return nums_lst

def max_prod_of_n_nums(nums_lst, n):
	if n % 2 == 0:
		new_nums = [abs(n) for n in nums]
		return reduce(lambda x,y: x*y, hq.nlargest(n, new_nums))
	else:
		a, b = hq.nlargest(n, nums), hq.nsmallest(n-1,nums)
		ans1 = reduce(lambda x, y: x*y, a)
		ans2 = reduce(lambda x, y: x*y, b)*a[0]
		return max(ans1, ans2)



def n_most_frequent_nums(numslsts, n):
	nums_lst = reduce(lambda x,y: x+y, numslsts)
	d = Counter(nums_lst)
	ans = hq.nlargest(n, d.items(), key = lambda x: x[1])
	return [n[0] for n in ans]

def n_most_expensive_cheapest_items(items_dict,n):
	return hq.nsmallest(n, items_dict, key = lambda x: x['price']),
	hq.nlargest(n, items_dict, key = lambda x: x['price'])


def merge_lsts(lst1,lst2,lst3):
	return list(hq.merge(lst1,lst2,lst3))

def find_kth_smallest_matrix_element(matrix,k):
	all_elements = set(reduce(lambda x,y: x+y, matrix))
	k_smallest_nums = hq.nsmallest(k, all_elements)
	return k_smallest_nums[-1]

def n_super_uglies(n, primes):
	uglies = [1]
	def gen(prime):
		for ugly in uglies:
			yield ugly * prime
	merged = hq.merge(*map(gen,primes))
	while len(uglies) < n:
		ugly = next(merged)
		if ugly != uglies[-1]:
			uglies.append(ugly)
	return [i for i in uglies if i != 1]

print(n_super_ugly_numbers(10, [2,3,5,7]))

def str_with_different_adjacent_chars(str1):
	ctr = Counter(str1)
	heap = [(-f, ch) for key, ch in ctr.items()]
	hq.heapify(heap)
	if (-heap[0][0]) * 2 > len(str1) + 1: # if twice the number of the most frequent char is larger than the length of the whole string plus 1:
		return ""
	ans = []
	#alternate chars
	while len(heap) >= 2: #as long as heap contains at least two different chars.
		f1, ch1 = hq.heappop(heap) #take the most frequent char out
		f2, ch2 = hq.heappop(heap) #take the second most frequent char out
		ans.extend([ch1, ch2]) #ans now contains the two most frequent chars
		# Replace items in heap, if a char occurs only once remove it from heap
		if nct1 + 1: hq.heappush(heap, (f1 + 1, ch1)) #if nct1 + 1 is not 0/ if nct1 occurs more than 1 time
		if nct2 + 1: hq.heappush(heap, (f2 + 1, ch2)) #if nct2 plus 1 is not 0/ if nct2 occurs more than 1 time
	return "".join(ans) + (heap[0][1] if heap else "")

####
# find median of an array of numbers

def find_median(nums_lst):
	length = len(nums)
	hq.heapify(nums)
	if len(nums) % 2 == 0:
		left_index = len(nums)//2 - 1
		right_index = left_index + 1
		return (nums[left_index]+nums[right_index])/2
	else:
		median_index = len(nums)/2 + 0.5 - 1
		return nums[median_index]

def spiralMatrix(matrix):
	R, C = len(matrix), len(matrix[0])
	seen = [[False]*C for _ in matrix]
	dr = [0,-1,0,-1]
	dc = [1,0,-1,0]
	r, c, di = 0
	for _ in range(R*C):
		ans.append(matrix[r][c])
		seen[r][c] = True
		cr, cc = r + dr[di], c + dc[di]
		if 0 <= cr < R and 0 <= cc < C and not seen[r][c]:
			r, c = cr, cc
		else:
			di = (di+1)%4
			r, c = r + dr[di], c + dc[di]
	return ans

def flipMatrix(matrix):
        
    n=len(matrix)-1

    for r in range(len(matrix)//2):
        matrix[r],matrix[n]=matrix[n],matrix[r]
        n-=1
    
    for r in range(len(matrix)):
        for c in range(r+1,len(matrix)):
            matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
    
    return matrix

print(flipMatrix([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

def zigzagConvert(s, numRows):
    ans = []
    n = len(s)
    cycle = numRows*2 - 2
    for i in range(numRows):
        for j in range(i, n, cycle):
            ans.append(s[j])
            if i != numRows-1 and i != 0 and j+cycle-2*i < n:
                ans.append(s[j+cycle-2*i])
    return ''.join(ans)

def maxArea(height):
    areas = []
    for i in range(len(height)):
        for j in range(i, len(height)):
            area = int(min(height[i],height[j]) * abs(i-j))
            areas.append(area)
    return max(areas, key = lambda x: len(x))    	

