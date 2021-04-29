from xml_parsing import Puzzle_XML
from sieving import *

class Grid:

	def __init__(self, puzzle_xml):
		self.grid = puzzle_xml.start_state
		self.rows_per_box = puzzle_xml.rows_per_box
		self.cols_per_box = puzzle_xml.cols_per_box
		self.grid_size = self.rows_per_box * self.cols_per_box
		self.sub_grids = puzzle_xml.sub_grids
		self.solved = False
		
	def step(self):
		k = 1
		
		while (k < self.grid_size):
			# Begin by going through each row
			for row in range(self.grid_size):
				# Fill current row
				row_cells = {}
				for col_index in range(self.grid_size):
					row_cells[(row, col_index)] = self.grid[(row, col_index)]
					
				# Get combinations
				for combo in get_combinations(k, list(row_cells.keys())):
					equal = True
					if k == 1 and len(self.grid[combo[0]]) == 1:
						values = self.grid[combo[0]]
					elif k == 1 and len(self.grid[combo[0]]) != 1:
						continue
					else:
						values = self.grid[combo[0]]
						for cell in combo:
							"""
							print(cell)
							print(len(self.grid[cell]))
							print(k)
							print(self.grid[cell])
							print(values)
							"""
							if len(self.grid[cell]) != k or self.grid[cell] != values:
								equal = False
								break
					
					if equal:
						for value in values:
							sieved = sieve(combo, row_cells, value, self)
							if sieved:
								return { "combo": combo, "value": value, \
										"cells_sieved": sieved, "row": row }
							
								
			# Go through each column
			for col in range(self.grid_size):
				# Fill current col
				col_cells = {}
				for row_index in range(self.grid_size):
					col_cells[(row_index, col)] = self.grid[(row_index, col)]
					
				# Get combinations
				for combo in get_combinations(k, list(col_cells.keys())):
					equal = True
					if k == 1 and len(self.grid[combo[0]]) == 1:
						values = self.grid[combo[0]]
					elif k == 1 and len(self.grid[combo[0]]) != 1:
						continue
					else:
						values = self.grid[combo[0]]
						for cell in combo:
							"""
							print(cell)
							print(len(self.grid[cell]))
							print(k)
							print(self.grid[cell])
							print(values)
							"""
							if len(self.grid[cell]) != k or self.grid[cell] != values:
								equal = False
								break
					
					if equal:
						for value in values:
							sieved = sieve(combo, col_cells, value, self)
							if sieved:
								return { "combo": combo, "value": value, \
										"cells_sieved": sieved, "col": col }
										
			# Go through each box
			#box_row = row // self.rows_per_box
			#box_col = col // self.cols_per_box
			
			for box in self.sub_grids.keys():
				# Fill current box
				box_cells = {}
				for cell in self.sub_grids[box]:
					box_cells[cell] = self.grid[cell]
				
					
				# Get combinations
				for combo in get_combinations(k, list(box_cells.keys())):
					equal = True
					if k == 1 and len(self.grid[combo[0]]) == 1:
						values = self.grid[combo[0]]
					elif k == 1 and len(self.grid[combo[0]]) != 1:
						continue
					else:
						values = self.grid[combo[0]]
						for cell in combo:
							if len(self.grid[cell]) != k or self.grid[cell] != values:
								equal = False
								break
					
					if equal:
						for value in values:
							sieved = sieve(combo, box_cells, value, self)
							if sieved:
								return { "combo": combo, "value": value, \
										"cells_sieved": sieved, "box": box }
			k += 1
			
		print("k = " + str(k))
		self.solved = True
		for value in self.grid.values():
			if len(value) != 1:
				self.solved = False
		
		return { "success" : self.solved }









"""
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
"""