import xml.etree.ElementTree as et
import re
from collections import OrderedDict

class Puzzle_XML:

	def __init__(self, xml_file):
		# Get element tree object
		tree = et.parse(xml_file)
		
		# Get the root element
		self.root = tree.getroot()
		
		# Fill in puzzle attributes
		self.name = self.root.find('name').text
		self.rows_per_box = self.get_rows_per_box()
		self.cols_per_box = self.get_cols_per_box()
		self.well_formed = self.root.find('well_formed').text
		self.solvable = self.root.find('solvable').text
		self.unique_solution = self.root.find('unique_solution').text
		self.pigeonhole = self.root.find('pigeonhole_decidable').text
		
		# Get the puzzle start state
		self.start_state = self.parse_puzzle_state()
		self.current_state = self.start_state
		self.sub_grids = self.get_sub_grids()
		
	def get_rows_per_box(self):
		rows_per_box = int(self.root.find('rows_per_box').text)
		if rows_per_box < 0:
			return 0
		else:
			return rows_per_box
	
	def get_cols_per_box(self):
		cols_per_box = int(self.root.find('cols_per_box').text)
		if cols_per_box < 0:
			return 0
		else:
			return cols_per_box
			
	def parse_puzzle_state(self):
		puzzle = self.root.find('start_state').text
		if not puzzle:
			puzzle = "{}"
		
		# Get rid of line break symbols and trim whitespace
		puzzle = puzzle.replace("\\", "")
		COMBINE_WHITESPACE = re.compile(r"\s+")
		stripped_puzzle = COMBINE_WHITESPACE.sub(" ", puzzle).strip()
		
		# Get the dictionary of start state puzzle
		puzzle_dict = OrderedDict()
		puzzle_dict = eval(stripped_puzzle)
		
		# Fills the empty cell values with values based on rows and columns
		empty_cell_vals = range(1, self.rows_per_box*self.cols_per_box + 1)
		
		# Fill the empty boxes with full list of optional values
		full_puzzle_dict = OrderedDict()
		for i in range(self.rows_per_box*self.cols_per_box):
			for j in range(self.rows_per_box*self.cols_per_box):
				if (i, j) not in puzzle_dict.keys():
					full_puzzle_dict[(i, j)] = list(empty_cell_vals)
				else:
					full_puzzle_dict[(i, j)] = puzzle_dict[(i, j)]
					
		return full_puzzle_dict
		
	def get_sub_grids(self):
		# Calculate number of sub-grids
		num_sub_grids = self.rows_per_box * self.cols_per_box
		
		start_row, start_col = 0, 0
		box_row, box_col = 0, 0
		sub_grids = {}
		
		while (start_row < num_sub_grids):
			for r in range(start_row, self.rows_per_box + start_row):
				for c in range(start_col, self.cols_per_box + start_col):
					if (box_row, box_col) in sub_grids.keys():
						sub_grids[(box_row, box_col)].append( (r, c) )
					else:
						sub_grids[(box_row, box_col)] = [ (r, c) ]
			if start_col + self.cols_per_box >= num_sub_grids:
				start_col = 0
				box_col = 0
				box_row += 1
				start_row += self.rows_per_box
			else:
				start_col += self.cols_per_box
				box_col += 1
		
		return sub_grids
		
	def __repr__(self):
		rep = "<?xml version=\"1.0\" ?>\n"
		rep += "<puzzle>\n"
		rep += "\t<name>" + self.name + "</name>\n"
		rep += "\t<rows_per_box>" + repr(self.rows_per_box) + "</rows_per_box>\n"
		rep += "\t<cols_per_box>" + repr(self.cols_per_box) + "</cols_per_box>\n"
		rep += "\t<start_state>\n"
		
		game_dict = {}
		
		for cell, value in self.current_state.items():
			if len(self.current_state[cell]) == 1:
				game_dict[cell] = self.current_state[cell]
				
		rep += str(game_dict) + "\n"
		rep += "\t</start_state>\n"
		rep += "\t<well_formed>" + self.well_formed + "</well_formed>\n"
		rep += "\t<solvable>" + self.solvable + "</solvable>\n"
		rep += "\t<unique_solution>" + self.unique_solution + "</unique_solution>\n"
		rep += "\t<pigeonhole_decidable>" + self.pigeonhole + "</pigeonhole_decidable>\n"
		rep += "</puzzle>"
		
		return rep
				

	"""
	#XML Variables
	rows_per_box = int(root.find('rows_per_box').text)
	if rows_per_box < 0:
		rows_per_box = 0
	cols_per_box = int(root.find('cols_per_box').text)
	if cols_per_box < 0:
		cols_per_box = 0
	name = root.find('name').text
	well_formed = root.find('well_formed').text
	solvable = root.find('solvable').text
	unique_solution = root.find('unique_solution').text
	pigeonhole = root.find('pigeonhole_decidable').text
	"""
	"""
	#if name is empty and solve on startup is present, dont look at solve on start
	if root.find('solve_on_startup') != None:
		if name != None:
			solve_on_start = root.find('solve_on_startup').text
	
	#if time delay is present and if name or solve on start up are both present then set time delay
	if root.find('time_delay') != None:
		if name != None or root.find('solve_on_startup') != None:
			time_delay = root.find('time_delay').text
			
	#if solution name is present and if name or solve on start up are both present then set solution name
	if root.find('solution_name') != None:
		if name != None or root.find('solve_on_startup') != None:
			solution_name = root.find('solution_name').text
			
	#if exit on solve is present and if name or solve on start up are both present then set exit on solve
	if root.find('exit_on_solve') != None:
		if root.find('solution_name') != None:
			if name != None or root.find('solve_on_startup') != None:
				exit_on_solve = root.find('exit_on_solve').text
	"""
	
	"""
	puzzle = root.find('start_state').text
	puzzle = puzzle.replace("\\", "")
	
	COMBINE_WHITESPACE = re.compile(r"\s+")
	stripped_puzzle = COMBINE_WHITESPACE.sub(" ", puzzle).strip()
	
	#print(stripped_puzzle)
	puzzle_dict = OrderedDict()
	puzzle_dict = eval(stripped_puzzle)
	print(puzzle_dict)
	print()
	
	full_puzzle_dict = OrderedDict()
	
	#Fills the empty cell values with values based on rows and columns
	empty_cell_vals = range(1,rows_per_box*cols_per_box + 1)
	print("This puzzles values: ")
	for i in empty_cell_vals:
		print(i)
	
	
	for i in range(rows_per_box*cols_per_box):
		for j in range(rows_per_box*cols_per_box):
			if (i, j) not in puzzle_dict.keys():
				full_puzzle_dict[(i, j)] = list(empty_cell_vals)
			else:
				full_puzzle_dict[(i, j)] = puzzle_dict[(i, j)]
				
				
	for key, value in full_puzzle_dict.items():
		print(key, value)
		
	print()
	print("puzzle name:" , name)
	print("rows:" , rows_per_box)
	print("columns:" , cols_per_box)
	print("well formed? :" , well_formed)
	print("solvable?:" , solvable)
	print("unique solution?: " , unique_solution)
	print("pidgeon hole?: " , pigeonhole)
	"""