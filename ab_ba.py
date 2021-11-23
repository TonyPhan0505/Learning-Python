# Trinh tu cong viec: duyet qua cac ky tu trong string va check neu ky tu ay va ky tu ngay sau no tao thanh "ab"
# hay "ba". Ban dau, so "ab" va so "ba" trong string deu bang 0. Neu khi duyet, tim duoc 1 "ab" thi tang so "ab"
# len 1. Neu tim duoc 1 "ba" thi tang so "ba" len 1. Cu the cho den khi duyet het tat ca cac ky tu tu vi tri 0
# den vi tri len(string)-1 cua string. Neu ta thay so "ab" tim duoc bang so "ba" tim duoc, ta khong can thay
# doi ky tu nao trong string, luu string vao tap hop ket qua. Neu so "ab" lon hon so "ba", ta can biet so "ab"
# lon hon so "ba" bao nhieu. Goi hieu so nay la d. 
# So "ab" va so "ba" chi co the chenh nhau nhieu nhat la 1. Suy ra d = 0 or d = 1. 
# Ta chi co the thay doi ky tu trong mot chuoi "ab" hoac "ba" neu chung nam o dau hoac cuoi
# string. Neu chuoi do o dau string, thi thay doi ky tu dau cua chuoi ay. Neu chuoi ay o cuoi string thi thay doi 
# ky tu cuoi cua chuoi ay.
# Neu d = 0, luu string vao tap hop ket qua. Neu d = 1 thi nhu sau. Neu so "ab" lon hon so "ba", tim "ab" o dau
# hoac cuoi. Neu "ab" o dau, doi a thanh b, neu "ab" o cuoi, doi b thanh a, chi can thay doi 1 ab, roi luu string
# da duoc thay doi vao tap hop ket qua. Neu so "ba" lon hon so "ab", tim "ba" o dau hoac cuoi string. Neu "ba" o dau
# thay doi b thanh a, neu ba o cuoi, thay doi a thanh b.

sotestcase = int(input())
results = []

for _ in range(sotestcase):
	string = [c for c in input()]
	if string == "":
		results.append("".join(string))
	else:
		so_ab = 0
		so_ba = 0
		for i in range(len(string)-1):
			if string[i] + string[i+1] == "ab":
				so_ab += 1
			elif string[i] + string[i+1] == "ba":
				so_ba += 1
		d = abs(so_ab - so_ba)
		if d == 0:
			results.append("".join(string))
		else:
			if so_ab > so_ba:
				if string[0] + string[1] == "ab":
					string[0] = "b"
				elif string[-2] + string[-1] == "ab":
					string[-1] = "a"
				
			elif so_ab < so_ba:
				if string[0] + string[1] == "ba":
					string[0] = "a"
				elif string[-2] + string[-1] == "ba":
					string[-1] = "b"
			
			results.append("".join(string))

for result in results:
	print(result)

