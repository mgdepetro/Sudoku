import sys
import argparse
from xml_parsing import Puzzle_XML
from sudoku_grid import Grid
from sieving import *

def main(argv):

	testing = True
	if testing:
		run_tests()
		return
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-P", "--PuzzleName", help="enter puzzle name we are using")
	parser.add_argument("-S", "--SolveOnStart", help="true or false to sollve on start")
	parser.add_argument("-T", "--TimeDelay", help="if there is a time delay")
	parser.add_argument("-N", "--SolutionName", help="name of the solution file")
	parser.add_argument("-E", "--ExitOnSolve", help="if we exit after solving or not")
	
	args = parser.parse_args()
	
	if args.PuzzleName:
		print("puzzle name: %s" % args.PuzzleName)
	if args.SolveOnStart:
		print("solve on start up: %s" % args.SolveOnStart)
	if args.TimeDelay:
		print("time delay: %s" % args.TimeDelay)
	if args.SolutionName:
		print("solution name: %s" % args.SolutionName)
	if args.ExitOnSolve:
		print("exit on solve: %s" % args.ExitOnSolve)
		
	puzzle_xml = Puzzle_XML(args.PuzzleName)
	game_grid = Grid(puzzle_xml)
	
def run_tests():
	puzzle_xml = Puzzle_XML('3x3_02_solvable.xml')
	game = Grid(puzzle_xml)
	step = 0
	
	while (True):
		result = game.step()
		step += 1
		print(" -- STEP " + str(step) + " -- ")
		#print(len(result["combo"]))
		if "success" not in result.keys():
			print(result)
			for cell in result["cells_sieved"]:
				if len(game.grid[cell]) < 1:
					print("I AM BROKENNNNNNNNNNNNNNNNNNNNNNNNN")
					break
		else:
			print(result["success"])
			break
		#print(result["cells_sieved"])
	
	print(" -- GRID -- ")
	for r in range(game.grid_size):
		print()
		for c in range(game.grid_size):
			print(str(game.grid[(r, c)]) + " ", end="")
	
	print()
	"""
	print(" -- SUB GRIDS -- ")
	for key, value in game.sub_grids.items():
		print(key, value)
	"""
	
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))