import math

# Data Collection
test_case = 1
over = False
inps = []
while test_case <= 1000 and not over:
	inp = [float(i) for i in input().split()]
	if inp == [0.0,0.0,0.0]:
		over = True
	else: inps.append(inp)
	test_case += 1

# Data Analysis
results = []

for inp in inps:
	r = inp[0]
	m = inp[1]
	c = inp[2]
	area_of_circle = math.pi * (r**2)
	area_of_square = (r*2)**2
	estimated_area = (area_of_square / m) * c
	results.append(f"{area_of_circle} {estimated_area}")

# Display Results
for result in results:
	print(result)
