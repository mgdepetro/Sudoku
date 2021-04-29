

def get_combinations(k, collection):
    if k <= 0:
        print("error")
    elif k > len(collection):
        return tuple(())
    elif k == 1:
        for value in collection:
            yield (value,)
    else:
        first_item = collection[0]
        residual = collection[1:]
        
        for combo in get_combinations(k - 1, residual):           
            yield (first_item,) + combo
        
        yield from get_combinations(k, residual)
		
def sieve(cells, cells_to_search, value, puzzle):
	sieved = []
	for cell in cells_to_search.keys():
		if cell in cells:
			continue
		if value in puzzle.grid[cell]:
			puzzle.grid[cell].remove(value)
			sieved.append(cell)
					
	return sieved
					
				
		
		
	"""
	puzzle_dict = game.grid
	value = puzzle_dict[cell][0]
	print("value = " + str(value))
	row = cell[0]
	col = cell[1]
	
	# Sieve from row
	for i in range(9):
		if i == col:
			continue
		elif value in puzzle_dict[(row, i)]:
			puzzle_dict[(row, i)].remove(value)
			return (row, i)
			
	# Sieve from column
	for i in range(9):
		if i == row:
			continue
		elif value in puzzle_dict[(i, col)]:
			puzzle_dict[(i, col)].remove(value)
			return (i, col)
			
	# Sieve from box
	# Determine which box this cell is in
	box_row = row // game.rows_per_box
	box_col = col // game.cols_per_box
	
	cells_in_box = game.sub_grids[(box_row, box_col)]
	
	for item in cells_in_box:
		if item == cell:
			continue
		if value in puzzle_dict[item]:
			puzzle_dict[item].remove(value)
	"""