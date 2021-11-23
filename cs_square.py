import math

sotestcase = int(input())
results = []
for _ in range(sotestcase):
	case = [int(i) for i in input().split()]
	r = case[0]
	n = case[1]
	if n > 0:
		ns = []
		rs = []
		for i in range(n):
			if i == 0:
				ns.append(1)
				rs.append(r)
			elif i == 1:
				ns.append(4)
			else:
				ns.append(ns[-1]*3)
			if i > 0:
				rs.append(rs[-1]/2)
		result = 0
		for r in range(len(rs)):
			result += (rs[r]**2) * math.pi * ns[r]
		results.append(result)
	else: results.append(0)

for result in results:
	print(result)