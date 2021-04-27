from xml_parsing import Puzzle_XML

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

""" TESTING
my_collection = [ 1, 2, 3, 4, 5, 6 ]
print( [i for i in get_combinations(1, my_collection)] )
"""
	
def sieve(cell, puzzle):
	puzzle_dict = puzzle.start_state
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
			
	# Sieve from column
	for i in range(9):
		if i == row:
			continue
		elif value in puzzle_dict[(i, col)]:
			puzzle_dict[(i, col)].remove(value)
			
	# Sieve from box
	# Determine which box this cell is in
	box_row = row // puzzle.rows_per_box
	box_col = col // puzzle.cols_per_box
	
	cells_in_box = puzzle.sub_grids[(box_row, box_col)]
	
	for item in cells_in_box:
		if item == cell:
			continue
		if value in puzzle_dict[item]:
			puzzle_dict[item].remove(value)


puzzle_xml = Puzzle_XML('3x3_02_solvable.xml')
puzzle_dict = puzzle_xml.start_state
#for key, value in puzzle_dict.items():
	#print(key, value)

row_cells = {}
for i in range(9):
	row_cells[(0, i)] = puzzle_dict[(0, i)]

print(row_cells)

combinations = [ i for i in get_combinations(1, list(row_cells.keys())) ]

print(combinations)

for combo in combinations:
	if len(puzzle_dict[combo[0]]) == 1:
		print(combo[0])
		sieve(combo[0], puzzle_xml)
		
for key, value in puzzle_dict.items():
	print(key, value)