cases = int(input())
results = []

for _ in range(cases):
	n_d_c_extra = [int(item) for item in input().split()]
	n = n_d_c_extra[0]
	number_of_dog_foods = n_d_c_extra[1]
	number_of_cat_foods = n_d_c_extra[2]
	number_of_extra_cat_foods = n_d_c_extra[3]
	row_input = input()
	dogs = row_input.count("D")

	if dogs == 0:
		results.append(f"Case #{_+1}: YES")
	elif number_of_dog_foods < dogs:
		results.append(f"Case #{_+1}: NO")
	else:
		last_dog = row_input.rindex("D")
		row_input = row_input[0:last_dog+1]
		dogs_fed = 0
		index = 0
		while number_of_cat_foods > -1 and number_of_dog_foods > 0 and dogs_fed < dogs:
			if row_input[index] == "C":
				number_of_cat_foods -= 1
			elif row_input[index] == "D":
				number_of_dog_foods -= 1
				number_of_cat_foods += number_of_extra_cat_foods
				dogs_fed += 1
			index += 1
		
		if dogs_fed == dogs:
			results.append(f"Case #{_+1}: YES")
		elif dogs_fed < dogs:
			results.append(f"Case #{_+1}: NO")

for result in results:
	print(result)
	

	
		