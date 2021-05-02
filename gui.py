import tkinter as tk
import time
import os
from xml_parsing import Puzzle_XML
from sudoku_grid import Grid
from sieving import *


class SudokuGUI(tk.Frame):

	def __init__(self, master, puzzle_name = None, solve_on_start = None, \
				time_delay = None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.master.geometry("")
		#second row
		self.messagetext = tk.StringVar()
		self.message = tk.Label(self, textvariable = self.messagetext, bg="PaleGreen1", anchor = "center", width = 100)
		self.messagetext.set("Default: No puzzle set")
		
		#button 
		self.puzzlename = tk.Button(self, text="Specify puzzle as file name: ", bg="light slate blue", command= self.savePuzzleName, width= 25)
		
		#text entry for puzzle button 
		self.pnEntry = tk.Entry(self, bd =5,width= 25)
		self.puzzlename.grid(row = 0, column = 0, pady = 2, sticky = "W")
		self.pnEntry.grid(row=0, column=1, pady = 2, sticky="W")
		if puzzle_name:
			self.pnEntry.insert(tk.END, puzzle_name)
			self.savePuzzleName()
		
		
		#button
		self.startState = tk.Button(self, text="Store puzzle state as: ", bg="light slate blue", command= self.saveStartState, width= 25)

		self.startEntry = tk.Entry(self, bd =5,width= 25)
		
		self.startState.grid(row =0, column = 2, pady = 2, sticky = "W")
		self.startEntry.grid(row = 0, column = 3, pady = 2, sticky = "W")

		self.message.grid(row = 1, column = 0, columnspan= 4, pady = 2)
		
		#step solver row 
		self.stepSolver = tk.Button(self, text="Step the solver",bg="medium slate blue", command = self.saveStep,width= 25)

		self.stepText = tk.StringVar()
		self.stepCount = tk.Label(self, textvariable = self.stepText, bg = "light blue",width= 25)
		self.stepText.set("Enter step count: ")

		self.stepCountEntry = tk.Entry(self, bd = 5,width= 25)

		self.timeText = tk.StringVar()
		self.timeDelay = tk.Label(self, textvariable = self.timeText, bg = "light blue",width= 25)
		self.timeText.set("Enter inter-step delay(s): ")

		self.timeDelayEntry = tk.Entry(self, bd = 5,width= 25)

		self.stepSolver.grid(row = 2, column = 0, sticky = "W")
		self.stepCount.grid(row = 2, column = 1, sticky = "W")
		self.stepCountEntry.grid(row = 2, column = 2, sticky = "W")
		self.timeDelay.grid(row = 2, column = 3, sticky = "W" )
		self.timeDelayEntry.grid(row = 2, column = 4, sticky = "W")
		
		#complete the puzzle row
		self.puzzleSolver = tk.Button(self, text="Complete the Puzzle",bg="tan1", command = self.completePuzzle,width= 25)

		self.stepCompleteText = tk.StringVar()
		self.timeDelayComplete = tk.Label(self, textvariable = self.stepCompleteText, bg = "salmon",width= 25)
		self.stepCompleteText.set("Enter inter-step delay (s): ")

		self.completeEntry = tk.Entry(self, bd = 5, width= 25)
		
		self.puzzleSolver.grid(row = 3, column = 0, pady = 2, sticky = "W")
		self.timeDelayComplete.grid(row = 3, column = 1, pady = 2, sticky = "W")
		self.completeEntry.grid(row = 3, column = 2,sticky = "W")
		
		#scrolling text box to display the steps text
		self.text = tk.Text(self)
		self.scroller = tk.Scrollbar(self, orient="vertical", command = self.text.yview)
		self.text.configure(yscrollcommand=self.scroller.set)
		
		#self.text.grid(row = 13, column = 1)
		self.scroller = tk.Scrollbar(self, orient="vertical")
		self.text = tk.Text(self, height = 5,yscrollcommand=self.scroller.set, bd = 10)

		self.text.grid(row = 4, column = 0, columnspan = 4, sticky = "W")
		
		self.grid_rowconfigure(0, weight = 1)
		self.grid_rowconfigure(1, weight = 2)
		self.grid_rowconfigure(2, weight = 1)
		self.grid_rowconfigure(3, weight = 1)
		
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(1, weight = 1)
		self.grid_columnconfigure(2, weight = 1)
		self.grid_columnconfigure(3, weight = 1)
		
	def fillGridLabels(self):
		self.rows = self.gameGrid.grid_size
		
		# Fill label dictionary
		self.cellLabelDict = {}
		for cell in self.gameGrid.grid.keys():
			self.cellLabelDict[cell] = tk.Label(self, bg = "white", width = 25, height = 4, pady = 2, padx = 2)
			
	def drawGrid(self):
		# Draw the grid
		currentRow = 5
		for row in range(self.gameGrid.grid_size):
			currentCol = 0
			for col in range(self.gameGrid.grid_size):
				self.cellLabelDict[(row, col)].grid(row = currentRow, column = currentCol)
				self.cellLabelDict[(row, col)].config(text = self.gameGrid.grid[(row, col)])
				
				currentCol += 1
			currentRow +=1
			
	def updateGrid(self):
		# Update the grid
		currentRow = 4
		for row in range(self.gameGrid.grid_size):
			currentCol = 0
			for col in range(self.gameGrid.grid_size):
				self.cellLabelDict[(row, col)].config(text = self.gameGrid.grid[(row, col)])
				currentCol += 1
			currentRow +=1
		
		                                                                                                                            
	def savePuzzleName(self):
		self.puzzlename = self.pnEntry.get()
		print("the name is: " + self.puzzlename)
		try:
			self.parseXML()
			self.displayPuzzleMessage()
		except FileNotFoundError:
			self.messagetext.set("?? can't load puzzle specification: No such file or directory: " + self.puzzlename)
		self.fillGridLabels()
		self.drawGrid()
	
	def displayPuzzleMessage(self):
		try:
			msg = self.puzzlename + " - is "
			if self.puzzleXML.well_formed == 'True':
				msg += "well-formed, "
			else:
				msg += "ill-formed, "
			if self.puzzleXML.solvable == 'True':
				msg += "solvable, "
			else:
				msg += "not solvable, "
			if self.puzzleXML.unique_solution == 'True':
				msg += "has a unique solution, "
			else:
				msg += "has multiple solutions, "
			if self.puzzleXML.pigeonhole == 'True':
				msg += "is pigeonhole-decidable."
			else:
				msg += "is not pigeonhole-decidable."
		except:
			self.messagetext.set("?? can't load puzzle specification: XML not in correct format.")
			return
			
		self.messagetext.set(msg)
	
	def parseXML(self):
		self.puzzleXML = Puzzle_XML(self.puzzlename)
		self.gameGrid = Grid(self.puzzleXML)
		self.step = 1
		
	def saveStartState(self):
		self.start = self.startEntry.get()
		if not self.start.endswith(".xml"):
			self.start += ".xml"
			
		if os.path.exists(self.start):
			self.messagetext.set("?? can't save puzzle specification: File already exists.")
			return
			
		with open(self.start, 'w+') as f:
			f.write(repr(self.puzzleXML))
			
		self.messagetext.set("File " + self.start + " created successfully.")
		
	def saveStep(self):
		try:
			self.stepCount = int(self.stepCountEntry.get())
			delay = self.timeDelayEntry.get()
			if delay:
				self.timeDelay = float(delay)
				if self.timeDelay < 0:
					raise ValueError
			else:
				self.timeDelay = 0
		except ValueError:
			self.messagetext.set("Invalid time delay. Enter a positive number.")
			return
			
		
		#print("time delay: " + str(self.timeDelay))
		if self.gameGrid.solved == False:
			self.doSteps(self.stepCount)
			
	def doSteps(self, count):
		for step in range(count):
			result = self.gameGrid.step()
			self.logStep(result)
			self.puzzleXML.current_state = self.gameGrid.grid
			self.step += 1
			self.updateGrid()
			if self.gameGrid.solved == True:
				return
			time.sleep(self.timeDelay)
			
			
	def logStep(self, result):
		# This is where the text box will update - add step info
		
		if "success" in result.keys():
			if result["success"] == True:
				self.messagetext.set(self.puzzlename + " solved successfully.")
			else:
				self.messagetext.set(self.puzzlename + " could not be solved.")
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
				string += "cell " + str(cell) + "\n"
			
			self.text.insert(tk.END, string)
		
		
	def completePuzzle(self):
		delay = self.completeEntry.get()
		try:
			if delay:
				self.timeDelay = float(delay)
				if self.timeDelay < 0:
					raise ValueError
			else:
				self.timeDelay = 0
		except ValueError:
			self.messagetext.set("Invalid time delay. Enter a positive number.")
			return
		
		while (not self.gameGrid.solved):
			result = self.gameGrid.step()
			self.logStep(result)
			self.step += 1
			time.sleep(self.timeDelay)