from re import L
import numpy as np
import math
from colorist import Color, red, blue, white, green, black, yellow, magenta, cyan
import time

file_words = open("capitals_names.dic")
file_grid = open("capitals_grid.dic")
grid = []
grid2 = []


L3 = []
L4 = []
content_grid = file_grid.readlines()
hidden_words = file_words.readlines()


def grid_lists():
	for line in content_grid:
		grid.append([line.replace("\n", "")])

	for x in range(len(grid)):
		grid2.append([])
		for y in range(len(grid)):
			grid2[x].append(grid[x][0][y])
	return [grid, grid2]


def words_list():
	words_to_find = []
	for w in hidden_words:
		words_to_find.append(w.replace("\n", ""))
		print(w.replace("\n", ""))
	print("Nombre de mots:", len(words_to_find))
	print('\n')
	return words_to_find


def check_grid():
	grids = grid_lists()
	grid = grids[0]
	grid2 = grids[1]
	words_to_find = words_list()
	n = len(grid)

	def check_vertontal_and_vertical_check():
		horizontals = []
		verticals = []
		found_words = []
		coord_vert = []
		coord_hor = []
		
		for i in range(n):
			for j in range(n):
				verticals.append(grid[j][0][i])

		for line in grid:
			for letter in line:
				horizontals.append(letter)
		stg_horizontals = ("").join(horizontals)
		stg_verticals = ("").join(verticals)
		stg_hor_ver = stg_horizontals + stg_verticals
		print("LEN STG:", len(stg_horizontals))
		for w in words_to_find:
			if w in stg_horizontals:
				found_words.append(w)
				coord_hor.append([stg_horizontals.index(w), len(w)])
				# print("hor",w)
				# print("coord:", coord_vert[-1])
				# print(stg_horizontals.index(w), len(w))
			if w[::-1] in stg_horizontals:
				found_words.append(w)
				coord_hor.append([stg_horizontals.index(w[::-1]), len(w)])
				# print("hor",w[::-1])
				# print("coord:", coord_vert[-1])
				# print(stg_horizontals.index(w[::-1]), len(w))
			
			if w in stg_verticals:
				found_words.append(w)
				coord_vert.append([stg_verticals.index(w), len(w)])
				# print("vert:",w)
				# print("coord:", coord_vert[-1])
				# print("ind_vert:",stg_verticals.index(w), len(w))
			if w[::-1] in stg_verticals:
				found_words.append(w)
				coord_vert.append([stg_verticals.index(w[::-1]), len(w)])
				# print("vert:",w[::-1])
				# print("coord:", coord_vert[-1])
				# print("ind_vert:", stg_verticals.index(w[::-1]), len(w))

				# stg_hor_ver = stg_hor_ver.replace(w[::-1], f"{Color.BLUE}{w[::-1]}{Color.OFF}")
		print("mots trouves vert et vert:", found_words)


		return [coord_hor, coord_vert, found_words]

# check_vertontal_and_vertical_check()


	def check_diagonals():
		n = len(grid)
		letters_licht = []
		found_words = []
		main_diag1_rev = []
		main_diag2_rev = []

		for y in range(n):
			for x in range(n):
				if x == y:
					main_diag1_rev.append(grid[y][0][x])
		# print("main_diag1_rev:",main_diag1_rev)
		for y in range(n):
			for x in range(n+1):
				if x == n-1-y:
					main_diag2_rev.append(grid[y][0][x])
		# print("main_diag2_rev:",main_diag2_rev)

		main_diag1_stg = (('').join(main_diag1_rev))[::-1]
		main_diag1 = []
		for c in main_diag1_stg:
			main_diag1.append(c)
		# print("main_diag1:", main_diag1)

		main_diag2_stg = (('').join(main_diag2_rev))[::-1]
		main_diag2 = []
		for c in main_diag2_stg:
			main_diag2.append(c)
		# print("main_diag2:", main_diag2)

		# matrix = np.array(grid)
		
		fdiag = [[] for _ in range(n*2 - 1)]
		bdiag = [[] for _ in range(len(fdiag))]
		min_bdiag = -n + 1
		fdiags_2 = []
		new_fdiag2 = []

		for x in range(n):
			for y in range(n):
				fdiag[x+y].append(grid2[y][x])
				bdiag[x-y-min_bdiag].append(grid2[y][x])

		fdiag_stgs = []
		coord_fdiags = []
		for licht in fdiag:
			licht = (''.join(licht))
			fdiag_stgs.append(licht)
		print('\n')
		for diag in fdiag_stgs:
			print((' ').join(diag))
		
		fdiag_stgs_all = ('').join(fdiag_stgs)
			# for letters in licht:
		# print("fdiag:",fdiag_stgs)
				# letters_licht.append(letters)
		# for licht in bdiag:
		# 	for letters in licht:
		# 		letters_licht.append(letters)
		# stg_diags = (''.join(letters_licht))
		# for w in words_to_find:
		for w in words_to_find:
			if w in fdiag_stgs_all:
			# 	found_words.append(w)
				fdiag_stgs_all = fdiag_stgs_all.replace(w, w.lower())
				# else:
				# 	fdiags_2.append(stg)
					# coord_fdiags.append([fdiag_stgs_all.index(w), len(w)])
					# print("fdiag_found_word:",w)
					# print(f"coord: index_w: {fdiag_stgs_all.index(w)} len_word: {len(w)}")
		print("\n")
		print(fdiag_stgs_all)
		print("\n")
		temp = []
		for x in range(0, len(fdiag_stgs_all), n):
			temp.append([fdiag_stgs_all[x:x+n]])

		new_fdiag = [[] for _ in range(n*2 - 1)]
		
		count = 0
		for x in range(len(fdiag)):
			new_fdiag[x].append(fdiag_stgs_all[count:count+len(fdiag[x])])
			count += len(fdiag[x])
		for l in new_fdiag:
			print(l)

		print("\n")


		test = []
		rebuilt_grid = []
		for x in range(n):
			rebuilt_grid.append([])

		for y in range(n):
			for x in range(n):
				if (y+x) <= n:
					rebuilt_grid[y].append(new_fdiag[y+x-1][0][-y])
				else:
					rebuilt_grid[y].append(new_fdiag[y+x-1][0][n-y])
		# for l in rebuilt_grid[1:]:
		# 	print(l)
		# print("\n")

		last = []
		
		for x in range(n):
			last.append(new_fdiag[-x][0][0])
		last = last[::-1]
		# print(last)

		rebuilt_grid.pop(0)
		rebuilt_grid.append(last)
		for l in rebuilt_grid:
			print(l)

		# for licht in rebuilt_grid:
		# 	licht = ('  '.join(licht))
		# 	print(licht)

		# 		stg_diags = stg_diags.replace(w, w.lower())
		# 	if w[::-1] in stg_diags:
		# 		found_words.append(w)
		# 		print("diag:", w)
		# 		stg_diags = stg_diags.replace(w[::-1], w.lower())
		
		print("mots trouves_diag:", len(found_words))
		print("\n")
		# print("LEN STG_DIAGS:", len(stg_diags))
		# print(stg_diags)
		# print('\n')
		return found_words

	# check_diagonals()

	coord_hor = check_vertontal_and_vertical_check()[0]
	coord_vert = check_vertontal_and_vertical_check()[1]

	missing = []
	found_words = check_vertontal_and_vertical_check()[2]
	found_words_diag = check_diagonals()
	found_words.extend(found_words_diag)
	print(found_words)
	print("len", len(found_words))
	print("\n")
	for w in words_to_find:
		if w not in found_words:
			missing.append(w)
	print("missing word:", missing)

	print("vertical:", coord_vert)
	print("\n")
	print("horizon:", coord_hor)
	len_index_hor = len(coord_hor)
	len_index_vert = len(coord_vert)
	coord_hor1 = []
	coord_vert1 = []
	coord_hor2 = []
	coord_vert2 = []
	for elem in coord_hor:
		# print(elem)
		elem[0] = [math.floor(elem[0]/n), elem[0]%n]
		# print(elem)
	# print("\n")
	for elem in coord_vert:
		# print(elem)
		elem[0] = [math.floor(elem[0]/n), elem[0]%n]
		# print(elem)
	print("\n")
	for x in range(n-len(coord_hor)):
		coord_hor.append([[0, 0], 0])
	# print("coord_hor:", coord_hor)
	# print("len:", len(coord_hor))
	# print("\n")
	for x in range(n-len(coord_vert)):
		coord_vert.append([[0, 0], 0])
	# print("coord_vert:", coord_vert)
	# print("len:", len(coord_vert))
	# print("\n")
	for x in range(n):
		coord_hor1.append([[0, 0], 0])
		coord_vert1.append([[0, 0], 0])
		coord_hor2.append([[0, 0], 0])
		coord_vert2.append([[0, 0], 0])

	# print("coord_hor2:", coord_hor2)
	# print("\n")
	# print("coord_vert2:", coord_vert2)
	# print("\n")

	

	for x in range(len_index_hor):
		if coord_hor[coord_hor[x][0][0]] != x:
			coord_hor1[coord_hor[x][0][0]] = coord_hor[x]
			
		# if coord_hor[x][0][0] != coord_hor[coord_hor[x][0][0]][0][0]:
		# 	coord_hor[coord_hor[x][0][0]] = coord_hor[x]
		# 	print('yes')

	for x in range(len_index_vert):
		# if coord_hor[coord_hor[x][0][0]] != 300:
		# 	print(coord_hor[coord_hor[x][0][0]])
		if coord_vert[coord_vert[x][0][0]] != x:
			coord_vert1[coord_vert[x][0][0]] = coord_vert[x]
			# print('yes')
	# print("coord_hor1:" , coord_hor1)
	# print("len:", len(coord_hor1))
	# print("\n")
	# print("coord_vert1:" , coord_vert1)
	# print("len:", len(coord_vert1))
	# print("\n")

	for x in range(len_index_vert):
		if coord_vert[x][0][0] == coord_vert1[coord_vert[x][0][0]][0][0] and coord_vert[x][0][1] != coord_vert1[coord_vert[x][0][0]][0][1]:
			# print("yes", coord_vert1[coord_vert[x][0][0]])
			coord_vert2[coord_vert[x][0][0]] = coord_vert[x]
	for x in range(len_index_hor):
		if coord_hor[x][0][0] == coord_hor1[coord_hor[x][0][0]][0][0] and coord_hor[x][0][1] != coord_hor1[coord_hor[x][0][0]][0][1]:
			# print("yes", coord_hor1[coord_hor[x][0][0]])
			coord_hor2[coord_hor[x][0][0]] = coord_hor[x]
			

	
	# print("coord_hor2_sup:" , coord_hor2)
	# print("len:", len(coord_hor2))
	# print("\n")
	print("coord_vert2:" , coord_vert2)
	print("len:", len(coord_vert2))
	# print(grid2)
	def display_resolved_grid():
		for y in range(n):
			print('')
			for x in range(n):
				if y == coord_hor1[y][0][0] and x in range(coord_hor1[y][0][1],coord_hor1[y][0][1]+coord_hor1[y][1]):
					print(f"{Color.RED}{grid2[y][x][0]}{Color.OFF}", end='  ')
				elif y == coord_hor2[y][0][0] and x in range(coord_hor2[y][0][1],coord_hor2[y][0][1]+coord_hor2[y][1]):
					print(f"{Color.RED}{grid2[y][x][0]}{Color.OFF}", end='  ')
				elif x == coord_vert1[x][0][0] and y in range(coord_vert1[x][0][1],coord_vert1[x][0][1]+coord_vert1[x][1]):
					print(f"{Color.BLUE}{grid2[y][x][0]}{Color.OFF}", end='  ')
				elif x == coord_vert2[x][0][0] and y in range(coord_vert2[x][0][1],coord_vert2[x][0][1]+coord_vert2[x][1]):
					print(f"{Color.BLUE}{grid2[y][x][0]}{Color.OFF}", end='  ')
				else:
					print(grid2[y][x][0], end='  ')

	display_resolved_grid()



check_grid()

