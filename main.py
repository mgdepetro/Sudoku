import sys
import getopt

def main(argv):
	argumentList = sys.argv[1:]

	options = "pstne:"

	long_options = ["Puzzle_Name", "Solve_On_Startup", "Time_Delay", "Solution_Name", "Exit_On_Solve"]
	print("hi")
	try:
		arguments, values = getopt.getopt(argumentList, options, long_options)
		
		for currentArgument, currentValue in arguments:
			if currentArgument in ("-p", "--Puzzle_Name"):
				print("puzzle name option")
			elif currentArgument in ("-s", "--Solve_On_Startup"):
				print("solve on start option")
			elif currentArgument in ("-t", "--Time_Delay"):
				print("time delay option")
			elif currentArgument in ("-n", "--Solution_Name"):
				print("solution name option")
			elif currentArgument in ("-e", "--Exit_On_Solve"):
				print("exit on solve option")
				
	except getopt.error as err:
		print(str(err))
	