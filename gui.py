import tkinter as tk
import time
from xml_parsing import Puzzle_XML
from sudoku_grid import Grid
from sieving import *


class SudokuGUI(tk.Frame):

	def __init__(self, master, puzzle_name = None, solve_on_start = None, \
				time_delay = None):
		super().__init__(master)
		self.master = master
		self.pack()
		
		#button 
		self.puzzlename = tk.Button(self, text="Specify puzzle as file name: ", bg="light slate blue", command= self.savePuzzleName)
		
		#text entry for puzzle button 
		self.pnEntry = tk.Entry(self, bd =5)
		self.puzzlename.grid(row = 0, column = 0, pady = 2)
		self.pnEntry.grid(row=0, column=1, pady = 2)
		if puzzle_name:
			self.pnEntry.insert(tk.END, puzzle_name)
			self.savePuzzleName()
		
		#button
		self.startState = tk.Button(self, text="Store puzzle state as: ", bg="light slate blue", command= self.saveStartState)

		self.startEntry = tk.Entry(self, bd =5)
		
		self.startState.grid(row =0, column = 2, pady = 2)
		self.startEntry.grid(row = 0, column = 3, pady = 2)
		
		#second row
		self.messagetext = tk.StringVar()
		self.message = tk.Label(self, textvariable = self.messagetext, bg="PaleGreen1")
		self.messagetext.set("Default: No puzzle set")

		self.message.grid(row = 1, column = 0, pady = 2)
		
		#step solver row 
		self.stepSolver = tk.Button(self, text="Step the solver",bg="medium slate blue", command = self.saveStep)

		self.stepText = tk.StringVar()
		self.stepCount = tk.Label(self, textvariable = self.stepText, bg = "light blue")
		self.stepText.set("Enter step count: ")

		self.stepCountEntry = tk.Entry(self, bd = 5)

		self.timeText = tk.StringVar()
		self.timeDelay = tk.Label(self, textvariable = self.timeText, bg = "light blue")
		self.timeText.set("Enter inter-step delay(s): ")

		self.timeDelayEntry = tk.Entry(self, bd = 5)

		self.stepSolver.grid(row = 2, column = 0)
		self.stepCount.grid(row = 2, column = 1)
		self.stepCountEntry.grid(row = 2, column = 2)
		self.timeDelay.grid(row = 2, column = 3)
		self.timeDelayEntry.grid(row = 2, column = 4)
		
		#complete the puzzle row
		self.puzzleSolver = tk.Button(self, text="Complete the Puzzle",bg="tan1", command = self.completePuzzle)

		self.stepCompleteText = tk.StringVar()
		self.timeDelayComplete = tk.Label(self, textvariable = self.stepCompleteText, bg = "salmon")
		self.stepCompleteText.set("Enter inter-step delay (s): ")

		self.completeEntry = tk.Entry(self, bd = 5)
		
		self.puzzleSolver.grid(row = 3, column = 0, pady = 2)
		self.timeDelayComplete.grid(row = 3, column = 1, pady = 2)
		self.completeEntry.grid(row = 3, column = 2)
		
	def savePuzzleName(self):
		self.puzzlename = self.pnEntry.get()
		print("the name is: " + self.puzzlename)
		self.parseXML()
		
	def parseXML(self):
		self.puzzleXML = Puzzle_XML(self.puzzlename)
		self.gameGrid = Grid(self.puzzleXML)
		self.step = 1
		
	def saveStartState(self):
		self.start = self.startEntry.get()
		print("the start state is: " + self.start)
		
	def saveStep(self):
		self.stepCount = int(self.stepCountEntry.get()) # ADD ERROR HANDLING
		#print("step count: " + str(self.stepCount))
		delay = self.timeDelayEntry.get()
		if delay:
			self.timeDelay = float(delay) # ADD ERROR HANDLING
		else:
			self.timeDelay = 0
		
		#print("time delay: " + str(self.timeDelay))
		if self.gameGrid.solved == False:
			self.doSteps(self.stepCount)
			
	def doSteps(self, count):
		for step in range(count):
			result = self.gameGrid.step()
			self.logStep(result)
			self.step += 1
			if self.gameGrid.solved == True:
				return
			time.sleep(self.timeDelay)
			
			
	def logStep(self, result):
		# This is where the text box will update - add step info
		
		if "success" in result.keys():
			print("done")
			return
		
		for cell in result["cells_sieved"]:
			string = ""
			string += "step " + str(self.step) + ": "
			string += "using " + str(result["combo"]) + " "
			if "set" in result.keys():
				string += "to set " + str(result["set"]) + " in "
				if "row" in result.keys():
					string += "row " + str(result["row"]) + ", "
				elif "col" in result.keys():
					string += "col " + str(result["col"]) + ", "
				else:
					string += "box " + str(result["box"]) + ", "
				string += "cell " + str(cell)
			else:
				string += "to remove " + str(result["value"]) + " from "
				if "row" in result.keys():
					string += "row " + str(result["row"]) + ", "
				elif "col" in result.keys():
					string += "col " + str(result["col"]) + ", "
				else:
					string += "box " + str(result["box"]) + ", "
				string += "cell " + str(cell)
			
			print(string)
		
		
	def completePuzzle(self):
		delay = self.completeEntry.get()
		if delay:
			self.timeDelay = float(delay) # ADD ERROR HANDLING
		else:
			self.timeDelay = 0
		#print("Complete steps: " + str(self.timeDelay))
		
		while (not self.gameGrid.solved):
			result = self.gameGrid.step()
			self.logStep(result)
			self.step += 1
			time.sleep(self.timeDelay)