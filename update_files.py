sotestcase = int(input())
results = []

for _ in range(sotestcase):
	n_k = [int(i) for i in input().split()]
	so_may_da_cai = 1
	so_may_chua_cai = n_k[0] - so_may_da_cai
	dong_ho = 0
	while so_may_chua_cai > 0:
		so_ket_noi = min(n_k[1], so_may_da_cai)
		dong_ho += 1
		so_may_da_cai += so_ket_noi
		so_may_chua_cai -= so_ket_noi

	results.append(dong_ho)

for result in results:
	print(result)


	


