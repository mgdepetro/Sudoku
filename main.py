import sys
import argparse

def main(argv):
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
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))