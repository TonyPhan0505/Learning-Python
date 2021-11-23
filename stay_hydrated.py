from functools import reduce

def stay_hydrated():

	cases = int(input())
	results = []
	for _ in range(cases):

		number_of_furnitures = int(input())
		furnitures = []
		for n_furniture in range(number_of_furnitures):
			f = [int(i) for i in input().split()]
			furniture = []
			for y in range(f[1],f[3]+1):
				for x in range(f[0],f[2]+1):
					edge_point = [x,y]
					furniture.append(edge_point)
			furnitures.append(furniture)
		
		all_x_coords = [point[0] for point in reduce(lambda x,y: x+y, furnitures)]
		all_y_coords = [point[1] for point in reduce(lambda x,y: x+y, furnitures)]

		min_x_coord = min(all_x_coords)
		max_x_coord = max(all_y_coords)
		
		min_y_coord = min(all_y_coords)
		max_y_coord = max(all_y_coords)

		search_area = []
		for y in range(min_y_coord, max_y_coord+1):
			for x in range(min_x_coord, max_x_coord+1):
				check_point = [x,y]
				search_area.append(check_point)
		
		all_paths = {}
		for point in search_area:
			point_to_furnitures = []
			for furniture in furnitures:
				all_paths_to_the_furniture = []
				for edger in furniture:
					horizontal_distance = abs(point[0]-edger[0])
					vertical_distance = abs(point[1]-edger[1])
					all_paths_to_the_furniture.append([horizontal_distance, vertical_distance])
				shortest_path_to_furniture = min(all_paths_to_the_furniture, key = lambda x: sum(x))
				point_to_furnitures.append(shortest_path_to_furniture)
			all_paths[tuple(point)] = point_to_furnitures
		
		shortest_path = min([sum(reduce(lambda x,y: x+y,item)) for item in all_paths.values()])
		suitable_positions = [item for item in all_paths.items() if sum(reduce(lambda x,y: x+y,item[1])) == shortest_path]

		if len(suitable_positions) > 1:
			x_distances = {}
			for item in suitable_positions:
				x_distance = sum([inner_item[0] for inner_item in item[1]])
				x_distances[item[0]] = x_distance
			least_x_distance = min(x_distances.values())
			suitable_positions_2 = [item for item in x_distances.items() if item[1] == least_x_distance]
			
			if len(suitable_positions_2) > 1:
				y_distances = {}
				for item in suitable_positions:
					y_distance = sum([inner_item[1] for inner_item in item[1]])
					y_distances[item[0]] = y_distance
					least_y_distance = min(y_distances.values())
				suitable_position_3 = [item for item in x_distances.items() if item[1] == least_x_distance][0][0]
				results.append(suitable_position_3)
				
			else:
				results.append(suitable_positions_2[0][0])
		else:
			results.append(suitable_positions[0][0])
	
	for r in range(len(results)):
		print(f"Case #{r+1}: {results[r][0]} {results[r][1]}")

stay_hydrated()