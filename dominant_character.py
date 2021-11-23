from collections import Counter

number_of_test_cases = int(input())
results = []
for _ in range(number_of_test_cases):
	s_length = int(input())
	s = input()
	sub_length = 0
	for x in range(s_length):
		for y in range(x+1,s_length):
			check = s[x:y+1]
			if Counter(check)['a'] > Counter(check)['b'] and Counter(check)['a'] > Counter(check)['c']:
				if len(check) < sub_length or sub_length == 0:
					sub_length = len(check)
	if sub_length:
		results.append(sub_length)
	else:
		results.append(-1)
for result in results:
	print(result)
