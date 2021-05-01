import tkinter as tk
class SudokuGUI(tk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.pack()
		
		#button 
		self.puzzlename = tk.Button(self, text="Specify puzzle as file name: ", bg="light slate blue", command= self.savePuzzleName)
		
		#text entry for puzzle button 
		self.pnEntry = tk.Entry(self, bd =5)
		
		self.puzzlename.grid(row = 0, column = 0, pady = 2)
		self.pnEntry.grid(row=0, column=1, pady = 2)
		
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
		
	def savePuzzleName():
		self.puzzlename = pnEntry.get()
		print("the name is: " + puzzlename)
		
	def saveStartState():
		self.start = startEntry.get()
		print("the start state is: " + start)
		
	def saveStep():
		self.stepCount = stepCountEntry.get()
		print("step count: " + stepCount)
		self.timeDelay = timeDelayEntry.get()
		print("time delay: " + timeDelay)
		
	def completePuzzle():
		self.completeStep = completeEntry.get()
		print("Complete steps: " + completeStep)