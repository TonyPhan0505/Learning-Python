# cho (x_bottom_left, y_bottom_left) va (x_top_right, y_top_right). x cao nhat la x_top_right. x thap nhat la
# x_bottom_left. y cao nhat la y_top_right. y thap nhat la y_bottom_left. Cac toa do bao quanh vat the la:
# (x_bottom_left,y_bottom_left),(x_bottom_left+1,y_bottom_left),(x_bottom_left+2,y_bottom_left), ... (x_top_right,y_bottom_left)
# (x_bottom_left, y_bottom_lef+1),(x_bottom_left+1,y_bottom_left+1),...(x_top_right, y_bottom)_left+1)
#.
#.
#.
# (x_bottom_left, y_top_right), (x_bottom_left+1, y_top_right),... (x_top_right, y_top_right)
# Quy luat: Vong duyet 1 la duyet y. Vong duyet 2 la duyet x. y duoc duyet tu y_bottom_left den y_top_right.
# x duoc duyet tu x_bottom_left den x_top_right.
# Khu vuc tiem kiem bat dau tu toa do (x_bottom_left_of_lowest_item,y_bottom_left_of_lowest_item) den (x_top_right_of_highest_item,y_top_right_of_highest_item)
# Cach tim toa do (x_bottom_left_of_lowest_item,y_bottom_left_of_lowest_item): (gia tri x nho nhat,gia tri y nho nhat)
# Cach tim toa do (x_top_right_of_highest_item,y_top_right_of_highest_item): (gia tri x lon nhat, gia tri y lon nhat)
# Quy luat: Vong duyet 1 la duyet 1. Vong duyet 2 la duyet x. Giong nhu quy luat truoc.
# Ta co tat ca toa do bao quanh cua moi vat the va tat ca cac toa do tim kiem. Khoang cach tu mot toa do tim kiem
# den mot toa do bao quanh mot noi that la toadotimkiem[0]-toadobaoquanh[0] + toadotimkiem[1]-toadobaoquanh[1].
# Nhu vay, tong quang duong phai di tu mot vi tri tim kiem den tat ca cac vat the la tong khoang cach giua vat
# the ay voi mot toa do bao quanh cua cac vat the. O moi vi tri tim kiem, ta chi tim khoang cach giua no va
# mot toa do bao quanh gan nhat voi no. Do se la gia tri min cua tap hop nhung khoang cach ma no tinh duoc. Ghi lai
# cac khoang cach gan nhat va tong cua tap hop cac khoang cach duoc ghi lai ay chinh la khoang cach giua vi tri
# tim kiem den tat ca cac vat the.


from functools import reduce

def stay_hydrated():

	cases = int(input())
	results = []
	for _ in range(cases):

		sonoithat = int(input())
		furnitures = []
		for noithat in range(sonoithat):
			f = [int(i) for i in input().split()]
			furniture = []
			for y in range(f[1],f[3]+1):
				for x in range(f[0],f[2]+1):
					toadobaoquanh = [x,y]
					furniture.append(toadobaoquanh)
			furnitures.append(furniture)
		
		tatcagiatrix = [toado[0] for toado in reduce(lambda x,y: x+y, furnitures)]
		tatcagiatriy = [toado[1] for toado in reduce(lambda x,y: x+y, furnitures)]

		giatrixnhonhat = min(tatcagiatrix)
		giatrixlonnhat = max(tatcagiatrix)
		
		giatriynhonhat = min(tatcagiatriy)
		giatriylonnhat = max(tatcagiatriy)

		khuvuctimkiem = []
		for y in range(giatriynhonhat,giatriylonnhat+1):
			for x in range(giatrixnhonhat,giatrixlonnhat+1):
				check_point = [x,y]
				khuvuctimkiem.append(check_point)
		
		tat_ca_quang_duong = {}
		for point in khuvuctimkiem:
			point_den_furnitures = []
			for furniture in furnitures:
				tat_ca_quang_duong_den_furniture = []
				for edger in furniture:
					quang_duong_ngang = abs(point[0]-edger[0])
					quang_duong_doc = abs(point[1]-edger[1])
					tat_ca_quang_duong_den_furniture.append([quang_duong_ngang, quang_duong_doc])
				quang_duong_ngan_nhat_den_furniture = min(tat_ca_quang_duong_den_furniture, key = lambda x: sum(x))
				point_den_furnitures.append(quang_duong_ngan_nhat_den_furniture)
			tat_ca_quang_duong[tuple(point)] = point_den_furnitures
		
		quang_duong_ngan_nhat = min([sum(reduce(lambda x,y: x+y,item)) for item in tat_ca_quang_duong.values()])
		cac_vi_tri_phu_hop = [item for item in tat_ca_quang_duong.items() if sum(reduce(lambda x,y: x+y,item[1])) == quang_duong_ngan_nhat]

		if len(cac_vi_tri_phu_hop) > 1:
			x_distances = {}
			for item in cac_vi_tri_phu_hop:
				x_distance = sum([inner_item[0] for inner_item in item[1]])
				x_distances[item[0]] = x_distance
			least_x_distance = min(x_distances.values())
			cac_vi_tri_phu_hop_he_2 = [item for item in x_distances.items() if item[1] == least_x_distance]
			
			if len(cac_vi_tri_phu_hop_he_2) > 1:
				y_distances = {}
				for item in cac_vi_tri_phu_hop:
					y_distance = sum([inner_item[1] for inner_item in item[1]])
					y_distances[item[0]] = y_distance
					least_y_distance = min(y_distances.values())
				vi_tri_phu_hop_he_3 = [item for item in x_distances.items() if item[1] == least_x_distance][0][0]
				results.append(vi_tri_phu_hop_he_3)
				
			else:
				results.append(cac_vi_tri_phu_hop_he_2[0][0])
		else:
			results.append(cac_vi_tri_phu_hop[0][0])
	
	for r in range(len(results)):
		print(f"Case #{r+1}: {results[r][0]} {results[r][1]}")

stay_hydrated()