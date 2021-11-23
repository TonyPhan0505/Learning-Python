# Thu thap thong tin
sodothi = 1
ketthuc = False
inps = []
while sodothi <= 100 and not ketthuc:
	sophantu = int(input())
	if sophantu != -1:
		dothi = []
		for _ in range(sophantu):
			dothi.append([int(i) for i in input().split()])
		inps.append(dothi)
		sodothi += 1
	else: ketthuc = True


# Tao ban do va tim weaks
results = []
for dothi in inps:
	size = len(dothi)
	graph = {}
	for thanhphan in range(size):
		graph[thanhphan] = []
	for r in range(size):
		for c in range(size):
			if dothi[r][c] == 1 and c not in graph[r]:
				graph[r].append(c)
	weaks = []
	for thanhphankiemtra in graph.keys():
		if not graph[thanhphankiemtra]:
			weaks.append(thanhphankiemtra)
		else:
			for phantuketnoi in graph[thanhphankiemtra]:
				if any(phantuketnoi2 for phantuketnoi2 in graph[phantuketnoi] if thanhphankiemtra in graph[phantuketnoi2]):
					break
				if phantuketnoi == graph[thanhphankiemtra][-1]:
					weaks.append(thanhphankiemtra)
	weaks.sort()
	weaks = " ".join([str(i) for i in weaks])
	results.append(weaks)

for result in results:
	print(result)
