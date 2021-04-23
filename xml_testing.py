import xml.etree.ElementTree as et
import re
from collections import OrderedDict

if __name__ == '__main__':
	# Get element tree object
	tree = et.parse('3x3_02_solvable.xml')
	
	# Get the root element
	root = tree.getroot()
	
	"""
	for child in root:
		print(child.tag, child.attrib)
		
	print()
	print([elem.tag for elem in root.iter()])
	"""
	
	# print(root.find('start_state').text)
	
	#XML Variables
	rows_per_box = int(root.find('rows_per_box').text)
	cols_per_box = int(root.find('cols_per_box').text)
	name = root.find('name').text
	well_formed = root.find('well_formed').text
	solvable = root.find('solvable').text
	unique_solution = root.find('unique_solution').text
	pigeonhole = root.find('pigeonhole_decidable').text
	
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
	
	#for i in range(9):
	#	for j in range(9):
	#		if (i, j) not in puzzle_dict.keys():
	#			full_puzzle_dict[(i, j)] = empty_cell_vals
	#		else:
	#			full_puzzle_dict[(i, j)] = puzzle_dict[(i, j)]
				
				
	#for key, value in full_puzzle_dict.items():
	#	print(key, value)
		
	print()
	print("puzzle name:" , name)
	print("rows:" , rows_per_box)
	print("columns:" , cols_per_box)
	print("well formed? :" , well_formed)
	print("solvable?:" , solvable)
	print("unique solution?: " , unique_solution)
	print("pidgeon hole?: " , pigeonhole)