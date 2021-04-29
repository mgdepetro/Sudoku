#!/usr/bin/python

import tkinter
from tkinter import *

window = tkinter.Tk()
window.geometry("800x125")
#methods for each button that save their values.
#not sure how to save to our variables yet from other classes but it will be what the .get() gets set to
def savePuzzleName():
	puzzlename = pnEntry.get()
	print("the name is: " + puzzlename)
def saveStartState():
	start = startEntry.get()
	print("the start state is: " + start)
def saveStep():
	stepCount = stepCountEntry.get()
	print("step count: " + stepCount)
	timeDelay = timeDelayEntry.get()
	print("time delay: " + timeDelay)
def completePuzzle():
	completeStep = completeEntry.get()
	print("Complete steps: " + completeStep)
	
#button 
puzzlename = Button(window, text="Specify puzzle as file name: ", bg="light slate blue", command= savePuzzleName)
puzzlename.pack( side = LEFT, anchor = NW, fill = X, expand = True)

#text entry for puzzle button 
pnEntry = Entry(window, bd =5)
pnEntry.pack(side = LEFT, anchor = NW, fill = X, expand = True)

#button
startState = Button(window, text="Store puzzle state as: ", bg="light slate blue", command= saveStartState)
startState.pack(side = LEFT, anchor = NE, fill = X, expand = True)

startEntry = Entry(window, bd =5)
startEntry.pack(side = LEFT, anchor= NE, fill = X, expand = True)

#second row
messagetext = StringVar()
message = Label(window, textvariable = messagetext, bg="PaleGreen1")
messagetext.set("Default: No puzzle set")
message.pack(expand = True, fill = X, side = LEFT, anchor = N);
message.place(y=25, width = 800)

#step solver row 
stepSolver = Button(window, text="Step the solver",bg="medium slate blue", command = saveStep)
stepSolver.pack(side = LEFT, anchor = W, fill = X, expand = True)
stepSolver.place(y = 45, width = 200)

stepText = StringVar()
stepCount = Label(window, textvariable = stepText, bg = "light blue")
stepText.set("Enter step count: ")
stepCount.pack(side = LEFT)
stepCount.place(y = 45, x = 200, width = 150, height = 25)

stepCountEntry = Entry(window, bd = 5)
stepCountEntry.pack(side = LEFT)
stepCountEntry.place(y = 45, x = 350, width = 150)

timeText = StringVar()
timeDelay = Label(window, textvariable = timeText, bg = "light blue")
timeText.set("Enter inter-step delay(s): ")
timeDelay.pack(side = LEFT)
timeDelay.place(y = 45, x = 500, height = 25, width = 150)

timeDelayEntry = Entry(window, bd = 5)
timeDelayEntry.pack(side = LEFT, expand = True, fill = X)
timeDelayEntry.place(y = 45, x = 650, width = 150)

#complete the puzzle row
puzzleSolver = Button(window, text="Complete the Puzzle",bg="tan1", command = completePuzzle)
puzzleSolver.pack(side = LEFT, anchor = W, fill = X, expand = True)
puzzleSolver.place(y = 70, width = 200)

stepCompleteText = StringVar()
timeDelayComplete = Label(window, textvariable = stepCompleteText, bg = "salmon")
stepCompleteText.set("Enter inter-step delay (s): ")
timeDelayComplete.pack(side = LEFT)
timeDelayComplete.place(y = 70, x = 200, width = 150, height = 25)

completeEntry = Entry(window, bd = 5)
completeEntry.pack(side = LEFT)
completeEntry.place(y = 70, x = 350, width = 150)

window.mainloop()