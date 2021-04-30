import tkinter as tk

class SudokuGUI(tk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.pack()
		
		#button 
		self.puzzlename = tk.Button(self, text="Specify puzzle as file name: ", bg="light slate blue", command= self.savePuzzleName)
		self.puzzlename.pack(side = tk.LEFT, anchor = tk.NW, fill = tk.X, expand = True)

		#text entry for puzzle button 
		self.pnEntry = tk.Entry(self, bd =5)
		self.pnEntry.pack(side = tk.LEFT, anchor = tk.NW, fill = tk.X, expand = True)

		#button
		self.startState = tk.Button(self, text="Store puzzle state as: ", bg="light slate blue", command= self.saveStartState)
		self.startState.pack(side = tk.LEFT, anchor = tk.NE, fill = tk.X, expand = True)

		self.startEntry = tk.Entry(self, bd =5)
		self.startEntry.pack(side = tk.LEFT, anchor= tk.NE, fill = tk.X, expand = True)

		#second row
		self.messagetext = tk.StringVar()
		self.message = tk.Label(self, textvariable = self.messagetext, bg="PaleGreen1")
		self.messagetext.set("Default: No puzzle set")
		self.message.pack(expand = True, fill = tk.X, side = tk.LEFT, anchor = tk.N);
		self.message.place(y=25, width = 800)

		#step solver row 
		self.stepSolver = tk.Button(self, text="Step the solver",bg="medium slate blue", command = self.saveStep)
		self.stepSolver.pack(side = tk.LEFT, anchor = tk.W, fill = tk.X, expand = True)
		self.stepSolver.place(y = 45, width = 1000)

		self.stepText = tk.StringVar()
		self.stepCount = tk.Label(self, textvariable = self.stepText, bg = "light blue")
		self.stepText.set("Enter step count: ")
		self.stepCount.pack(side = tk.LEFT)
		self.stepCount.place(y = 45, x = 1000, width = 150, height = 25)

		self.stepCountEntry = tk.Entry(self, bd = 5)
		self.stepCountEntry.pack(side = tk.LEFT)
		self.stepCountEntry.place(y = 45, x = 350, width = 150)

		self.timeText = tk.StringVar()
		self.timeDelay = tk.Label(self, textvariable = self.timeText, bg = "light blue")
		self.timeText.set("Enter inter-step delay(s): ")
		self.timeDelay.pack(side = tk.LEFT)
		self.timeDelay.place(y = 45, x = 500, height = 25, width = 150)

		self.timeDelayEntry = tk.Entry(self, bd = 5)
		self.timeDelayEntry.pack(side = tk.LEFT, expand = True, fill = tk.X)
		self.timeDelayEntry.place(y = 45, x = 650, width = 150)

		#complete the puzzle row
		self.puzzleSolver = tk.Button(self, text="Complete the Puzzle",bg="tan1", command = self.completePuzzle)
		self.puzzleSolver.pack(side = tk.LEFT, anchor = tk.W, fill = tk.X, expand = True)
		self.puzzleSolver.place(y = 70, width = 1000)

		self.stepCompleteText = tk.StringVar()
		self.timeDelayComplete = tk.Label(self, textvariable = self.stepCompleteText, bg = "salmon")
		self.stepCompleteText.set("Enter inter-step delay (s): ")
		self.timeDelayComplete.pack(side = tk.LEFT)
		self.timeDelayComplete.place(y = 70, x = 1000, width = 150, height = 25)

		self.completeEntry = tk.Entry(self, bd = 5)
		self.completeEntry.pack(side = tk.LEFT)
		self.completeEntry.place(y = 70, x = 350, width = 150)
		
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