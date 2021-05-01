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
							if len(self.grid[cell]) != k or self.grid[cell] != values:
								equal = False
								break
					
					if equal:
						for value in values:
							sieved = sieve(combo, row_cells, value, self)
							if sieved:
								return { "combo": combo, "value": value, \
										"cells_sieved": sieved, "row": row }
										
				# Check if any values are only present in one cell in current row
				dict_of_vals = {}
				for key, contents in row_cells.items():
					if len(contents) == 1:
						continue
					for val in contents:
						if val in dict_of_vals.keys():
							dict_of_vals[val] += 1
						else:
							dict_of_vals[val] = 1
				
				to_set = 0
				for num, count in dict_of_vals.items():
					if count == 1:
						to_set = num
						
				if to_set != 0:
					for cell in row_cells.keys():
						if to_set in self.grid[cell]:
							self.grid[cell] = [to_set]
							return { "combo": (cell,), "set": to_set, \
										"cells_sieved": [cell], "row": row }
			
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
							if len(self.grid[cell]) != k or self.grid[cell] != values:
								equal = False
								break
					
					if equal:
						for value in values:
							sieved = sieve(combo, col_cells, value, self)
							if sieved:
								return { "combo": combo, "value": value, \
										"cells_sieved": sieved, "col": col }
										
				# Check if any values are only present in one cell in current col
				dict_of_vals = {}
				for key, contents in col_cells.items():
					if len(contents) == 1:
						continue
					for val in contents:
						if val in dict_of_vals.keys():
							dict_of_vals[val] += 1
						else:
							dict_of_vals[val] = 1
				
				to_set = 0
				for num, count in dict_of_vals.items():
					if count == 1:
						to_set = num
						
				if to_set != 0:
					for cell in col_cells.keys():
						if to_set in self.grid[cell]:
							self.grid[cell] = [to_set]
							return { "combo": (cell,), "set": to_set, \
										"cells_sieved": [cell], "col": col }
										
			# Go through each box
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
										
				# Check if any values are only present in one cell in current box
				dict_of_vals = {}
				for key, contents in box_cells.items():
					if len(contents) == 1:
						continue
					for val in contents:
						if val in dict_of_vals.keys():
							dict_of_vals[val] += 1
						else:
							dict_of_vals[val] = 1
				
				to_set = 0
				for num, count in dict_of_vals.items():
					if count == 1:
						to_set = num
						
				if to_set != 0:
					for cell in box_cells.keys():
						if to_set in self.grid[cell]:
							self.grid[cell] = [to_set]
							return { "combo": (cell,), "set": to_set, \
										"cells_sieved": [cell], "box": box }
			
			k += 1
			
		self.solved = True
		for value in self.grid.values():
			if len(value) != 1:
				self.solved = False
		
		return { "success" : self.solved }