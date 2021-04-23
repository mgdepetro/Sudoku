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

puzzle = Puzzle_XML('3x3_02_solvable.xml')
print(puzzle.start_state)