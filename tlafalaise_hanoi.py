# Lafalaise, Tedros
# This implementation takes user input (the number of discs) and creates a new window where the computer
# automatically plays the Tower of Hanoi problem.
# This program does not require any other dependencies aside from tkinter.

from tkinter import *

numDiscs = int(input("How many discs do you want to use? "))

root = Tk()

screen = Canvas(root, width=1280, height=720, bg="white")
screen.pack(pady=20)

# Creating the pegs on the screen
sp_x = 65
sp_y = 120
start_peg = screen.create_rectangle(sp_x, sp_y, sp_x + 20, sp_y + (numDiscs * 40), fill="brown")

tp_x = 300
tp_y = 120
temp_peg = screen.create_rectangle(tp_x, tp_y, tp_x + 20, tp_y + (numDiscs * 40), fill="brown")

fp_x = 535
fp_y = 120
finish_peg = screen.create_rectangle(fp_x, fp_y, fp_x + 20, fp_y + (numDiscs * 40), fill="brown")

# Init the discs
discs = dict()
for i in range(numDiscs):
    num = i + 1
    x = 50
    y = 160 + (num * 20)
    discs[i] = screen.create_rectangle(x - (i * 10), y, x + (num * 25), y + 20, fill="blue")

# Functions to move discs from peg to peg
def toStart(num):
    screen.moveto(discs[num], 50 - (num * 20), 180 + (num * 20))

def toTemp(num):
    screen.moveto(discs[num], 285 - (num * 20), 180 + (num * 20))

def toFinish(num):
    screen.moveto(discs[num], 520 - (num * 20), 180 + (num * 20))

pegNames = ['Starting', 'Temp', 'Finishing']
pegs = [[x for x in range(numDiscs, 0, -1)], [], []]
numMoves = 0

# Recursive function to solve tower
def solveTower(n, start, temp, finish):
    global numMoves
    if n == 1:
        var = IntVar(root)
        root.after(600, var.set, 1)
        root.wait_variable(var)

        top = pegs[start].pop()
        print("Disc", top, "is moved from", pegNames[start], "peg to", pegNames[finish], "peg.")
        if finish == 0:
            toStart(top - 1)
        elif finish == 1:
            toTemp(top - 1)
        else:
            toFinish(top - 1)
        pegs[finish].append(top)
        numMoves += 1
        return
    solveTower(n - 1, start, finish, temp)

    var = IntVar(root)
    root.after(600, var.set, 1)
    root.wait_variable(var)

    top = pegs[start].pop()
    print("Disc", top, "is moved from", pegNames[start], "peg to", pegNames[finish], "peg.")
    if finish == 0:
        toStart(top - 1)
    elif finish == 1:
        toTemp(top - 1)
    else:
        toFinish(top - 1)
    pegs[finish].append(top)
    numMoves += 1
    solveTower(n - 1, temp, start, finish)
    return

solveTower(numDiscs, 0, 1, 2)
print("This tower took", numMoves, "moves to solve.")

root.mainloop()