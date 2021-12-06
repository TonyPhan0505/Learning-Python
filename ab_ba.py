n_test_case = int(input())
results = []

for _ in range(n_test_case):
	string = [c for c in input()]
	if string == "":
		results.append("".join(string))
	else:
		n_ab = 0
		n_ba = 0
		for i in range(len(string)-1):
			if string[i] + string[i+1] == "ab":
				n_ab += 1
			elif string[i] + string[i+1] == "ba":
				n_ba += 1
		d = abs(n_ab - n_ba)
		if d == 0:
			results.append("".join(string))
		else:
			if n_ab > n_ba:
				if string[0] + string[1] == "ab":
					string[0] = "b"
				elif string[-2] + string[-1] == "ab":
					string[-1] = "a"
				
			elif n_ab < n_ba:
				if string[0] + string[1] == "ba":
					string[0] = "a"
				elif string[-2] + string[-1] == "ba":
					string[-1] = "b"
			
			results.append("".join(string))

for result in results:
	print(result)

