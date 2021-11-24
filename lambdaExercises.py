from functools import reduce
from collections import Counter
from collections import defaultdict
import math
import random

def addTwoNums(x,y):
	result = lambda x,y: x+y
	return result(float(x),float(y))

def multiplyTwoNums(x,y):
	result = lambda x,y: x*y
	return result(float(x),float(y))

def ascSortArray(array):
	return array.sort(key = lambda x:x[1])

def desSortArray(array):
	return array.sort(key = lambda x:x[1], reverse = True)

def ascSortDict(dict,name):
	return sorted(dict, key = lambda x: x[name])

def findEvenNums(nums_list):
	return list(filter(lambda x: x%2 == 0, nums_list))

def findOddNums(nums_list):
	return list(filter(lambda x: x%2 != 0, nums_list))

def squareNumsInList(nums_list):
	return list(map(lambda x: x**2, nums_list))

def cubeNumsInList(nums_list):
	return list(map(lambda x: x**3, nums_list))

def checkPrefix(str1,prefix):
	result = lambda x: True if x.startswith(prefix) else False
	return result(str1)

def extractYearMonthDateTime(time_info):
	year = lambda x: x.year
	month = lambda x: x.month
	day = lambda x: x.day
	t = lambda x: x.time()
	return year(time_info), month(time_info), day(time_info), t(time_info)

def isDigit(num):
	result = lambda x: True if x.isdigit() else False
	return result(num)

def createFibonacciSeriesUpTo(n):
	series = lambda n: reduce(lambda x, _: x+[x[-2]+x[-1]],range(n-2),[0,1])
	return series(n)

def intersection(nested_lst, nums_lst):
	return list(map(lambda x: listed(filter(lambda y: y in nums_lst, x)), nested_lst))
	
def removeNoneValuesInArray(array):
	result = list(filter(lambda x: x != None, array))
	return result

def countEvenOddInArray(array):
	even_ctr = len(list(filter(lambda x: x%2 == 0, array)))
	odd_ctr = len(list(filter(lambda x: x%2 != 0, array)))
	return even_ctr, odd_ctr

def addTwoLists(lst1,lst2):
	result = list(map(lambda x, y: x+y, array1, array2))
	return result

def find_second_lowest_score(students_dict):
	students_lst = list(students_dict.items())
	ordered_student_list = sorted(students_list, key = lambda x: int(x[1]))
	for i in range(len(ordered_student_list)):
		if ordered_student_list[i][1] != ordered_student_list[0][1]:
			return ordered_student_list[i][1]
			break

def is_divisible_by_nineteen(nums_lst):
	result = list(filter(lambda x: x%19 == 0, nums_lst))
	return result

def find_palindroms(str_lst):
	result = list(filter(lambda x: x == x[::-1], str_lst))
	return result



def get_anagrams(words_source):
	d = defaultdict(list)
	for word in words_source:
		key = "".join(sorted(word))
		d[key].append(word)
	return d

def print_anagrams(words_source):
	d = get_anagrams(words_source)
	result = [i[1] for i in anagrams.items() if len(i[1]) > 1]
	return result

def find_numbers_larger_than_numsLstLength(str1):
	words = str1.split()
	arranged_digits = []
	nums = []
	for word in words:
		digits = list(filter(lambda x: x.isdigit() == True, word))
		arranged_digits.append(digits)
	for i in arranged_digits:
		if i != []:
			num = int("".join(i))
			nums.append(num)
	return list(filter(lambda x: x > len(nums),nums))

def multiply_elements_with_target(num_lst,target):
	result = list(map(lambda x: x*target, num_lst))
	return result

def sum_lengthsOfNames(names_lst,letter):
	names_lst = list(filter(lambda x: x.lower() and x.startswith(letter) == False, names_lst))
	lengths = list(map(lambda x: len(x),names_lst))
	return sum(lengths)

def sums_of_negatives_and_positives(num_lst):
	negatives = list(filter(lambda x: x<0, num_lst))
	positives = num_lst - negatives
	return sum(negatives), sum(positives)

def numbers_divisible_by_its_digits(start_num, end_num):
	result = [n for n in range(start_num,end_num+1) if not any (map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
	return result

def rearrange_next_bigger(n):
	digits = list(str(n))
	for i in range(len(digits)-2,-1,-1):
		if digits[i] < digits[i+1]:
			z = digits[i:]
			y = min(filter(lambda x: x > z[0],z))
			z.remove(y)
			sorted(z)
			digits[i:] = [y] + z
			return int("".join(digits))
	return 'No possible answer'

def max_len_lst(lst_ofNumLists):
	result = max(lst_ofNumLists, key = lambda x: len(x))
	return result

def sort_sublists(input_lst):
	result = [sorted(x, key = lambda x: x[0]) for x in input_lst]

def sort_lsts_by_length_and_value(input_list):
	return sorted(input_lst, key = lambda x: (len(x), x))

def max_num_in_mixed_lst(mixed_lst):
	max_val = max(mixed_lst, key = lambda x: (isinstance(x,int),x))
	return max_val

def sort_sum(input_matrix):
	result = sorted(input_matrix, key = lambda x: sum(x))
	return result

def filter_string_len(input_lst, length):
	result = list(filter(lambda x: len(x) == length, input_lst))
	return result

def count_float_values(input_lst):
	result = len(list(filter(lambda x: isinstance(x,float), input_lst)))
	return result

def checkString(str1):
	messg = [
		lambda str1: any(x.isupper() for x in str1) or 'String must contain at least 1 uppercase',
		lambda str1: any(x.islower() for x in str1) or 'String must contain at least 1 lowecase',
		lambda str1: any(x.isdigit() for x in str1) or 'String must contain at least 1 number',
		lambda str1: len(str1) >= 7 or 'String must be at least 7 chars long'
	]
	result = [x for x in [i(str1) for i in messg] if x != True]
	if not result:
		result.append('Valid String')
	return result

def filter_height_weight(students_dict):
	result = dict(filter(lambda x: x[1][0]>=6 and x[1][1]>=70, students_dict.items()))
	return result

def is_sorted_lst(input_lst, key = lambda x: x):
	for (index,num) in enumerate(input_lst[1:]):
		if key(num) < key(input_lst[index]):
			return False
	return True

def extract_nthElements_tuple(input_lst,n):
	result = list(map(lambda x: x[n],input_lst))
	return result

def sortListByAnIndex(input_lst,i):
	new_lst = sorted(input_lst, key = lambda x: x[i])
	return new_lst

def removeSubList(all_lst,sub_lst):
	new_lst = list(filter(lambda x: x not in sub_lst, all_lst))
	return new_lst

def find_elements_contain_substring(input_lst,substring):
	result = list(filter(lambda x: substring in x, input_lst))
	return result

def find_nested_lst_elements(lst1,lst2):
	result = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
	return result

def reverse_items_in_lst(input_lst):
	result = list(map(lambda x: x[::-1],input_lst))
	return result

def product_of_lst(input_lst):
	result = reduce(lambda x,y: x*y, input_lst)
	return result

def avg_tuples(input_tuple):
	result = tuple(map(lambda x: sum(x)/len(x),zip(*input_tuple)))
	return result

def extract_convert_numbers(input_tuple):
	result = tuple(map(lambda x: (int(x[0]), int(x[2])), input_tuple))
	return result

def max_min_indices(nums_lst):
	max_result = max(enumerate(nums_lst), key = lambda x: x[1])
	min_result = min(enumerate(nums_lst), key = lambda x: x[1])	
	return max_result, min_result

def sort_mixed_list(mixed_list):
	result = sorted(mixed_list,key = lambda e: (isinstance(e,str),e))
	return result

def sort_strNums(nums_lst):
	new_lst = sorted(nums_lst, key = lambda el: int(el))
	return new_lst

def count_elements_occurences(input_lst):
	result = dict(Counter(input_lst))
	return result

def count_elements_occurences(input_lst):
	result = dict(map(lambda el: (el, input_lst.count(el)), input_lst))
	return result

def remove_words(words_lst, removing_words):
	result = list(filter(lambda x: x not in removing_words, words_lst))
	return result

def max_min_list_tuples(class_students):
	return_max = max(class_students, key = lambda item: item[1])[1]
	return_min = min(class_students, key = lambda item: item[1])[1]
	return return_max, return_min

def sortMixedLst(lst):
	lst.sort(key = lambda x: (isinstance(x,str), x))
	return lst

def best_apartment_block(Blocks,Reqs):
	distances = dict()
	for i in range(len(Blocks)):
		distances_lst = [0]*len(Reqs)
		for k in Reqs:
			analysis = list(filter(lambda x: x!=Blocks[i],Blocks))
			for j in analysis:
				if j[k] == True:
					temp = []
					temp.append(abs(i - Blocks.index(j)))
					distances_lst[Reqs.index(k)] = min(temp)
	distances[i] = abs(reduce(lambda x,y: x-y,distances_lst))
	return min(distances.items(),key = lambda x: x[1])[0]

def nNumsWithSumEqualObj(lst, obj, n):
    temp = []
    for i in lst:
        items = [i] * n
        temp.extend(items)
    combos = []
    total_combos = int(math.factorial(len(temp))/(math.factorial(len(temp) - n) * math.factorial(n)))
    while len(combos) < total_combos:
        sample = random.sample(temp, k = n)
        if sample not in combos:
            combos.append(sample)
    ans = list(filter(lambda x: sum(x) == obj, combos))
    return ans if ans else None

lst = [1,2,3,4,5,6,7]
obj = 15
n = 3
print(nNumsWithSumEqualObj(lst, obj, n))