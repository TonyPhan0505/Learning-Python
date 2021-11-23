from itertools import combinations

sotestcase = int(input())
results = []

for _ in range(sotestcase):

	# Thu thap thong tin
	n_m = [int(i) for i in input().split()]
	so_row = n_m[0]
	so_cot = n_m[1]
	bang = []
	for r in range(so_row):
		bang.append([int(item) for item in input().split()])

	tap_hop_hang_do_hop_le = []

	so_hang_do_max = so_row - 1
	so_cot_trai_max = so_cot - 1
	so_cot_trai = 1
	so_cot_trai_khong_co_loi = False
	while so_cot_trai <= so_cot_trai_max and so_cot_trai_khong_co_loi == False:

		###########################################################################
		# Tao bang ben trai
		bang_ben_trai = [[] for _ in range(so_row)]
		for r in range(len(bang)):
			for c in range(so_cot_trai):
				bang_ben_trai[r].append(bang[r][c])
		
		# Tao bang ben phai
		bang_ben_phai = [[] for _ in range(so_row)]
		for r in range(len(bang)):
			for c in range(so_cot_trai, so_cot):
				bang_ben_phai[r].append(bang[r][c])
		
		###########################################################################

		# To mau va duyet truong hop
		tat_ca_cac_hang = [h for h in range(so_row)]
		so_hang_do_khong_co_loi = False
		for so_hang_do in range(1, so_hang_do_max+1):
			combo_khong_co_loi = False
			tat_ca_combo_hang_mau_do = [list(hang) for hang in list(combinations(tat_ca_cac_hang, so_hang_do))]
			for combo_hang_mau_do in tat_ca_combo_hang_mau_do:

				# Xac nhan co phat hien loi hay khong
				co_loi = False

				# Tap hop tat ca cac phan tu do ben trai
				tat_ca_items_do_ben_trai = set()
				# Tap hop tat ca cac phan tu do ben phai
				tat_ca_items_do_ben_phai = set()
				# Tap hop tat ca phan tu xanh ben trai
				tat_ca_items_xanh_ben_trai = set()
				# Tap hop tat ca phan tu xanh ben phai
				tat_ca_items_xanh_ben_phai = set()

				# To mau va luu cac phan tu mau do o hai ben bang
				for hang in combo_hang_mau_do:
					# To mau do ben trai va luu cac phan tu do ben trai
					for item in bang_ben_trai[hang]:
						tat_ca_items_do_ben_trai.add(item)
					# To mau do ben phai va luu cac phan tu do ben phai
					for item in bang_ben_phai[hang]:
						tat_ca_items_do_ben_phai.add(item)
				
				# To mau va luu cac phan tu mau xanh o hai ben bang
				combo_hang_mau_xanh = [h for h in tat_ca_cac_hang if h not in combo_hang_mau_do]
				for hang in combo_hang_mau_xanh:
					# To mau xanh ben trai va luu cac phan tu xanh ben trai
					for item in bang_ben_trai[hang]:
						tat_ca_items_xanh_ben_trai.add(item)
					# To mau xanh ben phai va luu cac phan tu xanh ben phai
					for item in bang_ben_phai[hang]:
						tat_ca_items_xanh_ben_phai.add(item)

				# Duyet cac phan tu o hai ben bang.
				# Duyet bang ben trai:
				for item_do in tat_ca_items_do_ben_trai:
					for item_xanh in tat_ca_items_xanh_ben_trai:
						if item_xanh > item_do:
							co_loi = True
							break
					if co_loi:
						break
				# Duyet bang ben phai khi khong tim thay loi ben trai
				if not co_loi:
					for item_xanh in tat_ca_items_xanh_ben_phai:
						for item_do in tat_ca_items_do_ben_phai:
							if item_do > item_xanh:
								co_loi = True
								break
						if co_loi:
							break
				
				if not co_loi: 
					combo_khong_co_loi = True
					tap_hop_hang_do_hop_le = combo_hang_mau_do
					break

			if combo_khong_co_loi:
				so_hang_do_khong_co_loi = True
				break

		# ###########################################################################
		if so_hang_do_khong_co_loi:
			so_cot_trai_khong_co_loi = True
		so_cot_trai += 1
	
	if so_cot_trai_khong_co_loi:
		trinh_tu_mau = []
		tap_hop_cac_hang_xanh_hop_le = [i for i in range(so_row) if i not in tap_hop_hang_do_hop_le]
		for i in tap_hop_hang_do_hop_le:
			trinh_tu_mau.insert(i, "R")
		for i in tap_hop_cac_hang_xanh_hop_le:
			trinh_tu_mau.insert(i, "B")
		trinh_tu_mau = "".join(trinh_tu_mau)
		so_cot_trai = so_cot_trai - 1
		results.append(["YES", f"{trinh_tu_mau} {so_cot_trai}"])
	else:
		results.append(["NO"])

for result in results:
	for e in result:
		print(e)
			

		

		
		
				






