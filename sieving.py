

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