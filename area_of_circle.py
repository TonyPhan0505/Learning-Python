import math

# Thu thap du lieu
sotestcase = 1
ketthuc = False
inps = []
while sotestcase <= 1000 and not ketthuc:
	inp = [float(i) for i in input().split()]
	if inp == [0.0,0.0,0.0]:
		ketthuc = True
	else: inps.append(inp)
	sotestcase += 1

# Tinh toan va thu thap ket qua
results = []

for inp in inps:
	r = inp[0]
	m = inp[1]
	c = inp[2]
	dientichhinhtron = math.pi * (r**2)
	dientichhinhvuong = (r*2)**2
	estimatedarea = (dientichhinhvuong / m) * c
	results.append(f"{dientichhinhtron} {estimatedarea}")

# In ket qua
for result in results:
	print(result)
