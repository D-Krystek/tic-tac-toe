import random
import tkinter as tk
board = [['','',''],['','',''],['','','']]
position_x = 0 
position_y = 0
over = False
col1 = [board[0][0],board[0][1], board[0][2]]
col2 = [board[1][0],board[1][1], board[1][2]]
col3 = [board[2][0],board[2][1], board[2][2]]
diag1 = [board[0][2], board[1][1],board[2][0]]
diag2 = [board[0][0], board[1][1],board[2][2]]
playerChar = 'X'
AIChar = 'O'
twoPlayer = False
def printBoard():
    global col1, col2, col3, diag1, diag2
    col1 = [board[0][0],board[1][0], board[2][0]]
    col2 = [board[0][1],board[1][1], board[2][1]]
    col3 = [board[0][2],board[1][2], board[2][2]]
    diag1 = [board[0][2], board[1][1],board[2][0]]
    diag2 = [board[0][0], board[1][1],board[2][2]]
    for each in board:
        print(each)
def endGame():
    #TODO Clean up checking method to board[0][0] == board[0][1] == board[0][2] format
    global over
    #if one row = X
    length = len(board)-1
    while(length >= 0):
        if board[length] == ['X','X','X']:
            print('Player X wins!')
            over = True
            length -= 1
        else:
            length -= 1
    #if one column = X
    if col1 == ['X','X','X']:
        print('Player X wins!')
        over = True
    if col2 == ['X','X','X']:
        print('Player X wins!')
        over = True
    if col3 == ['X','X','X']:
        print('Player X wins!')
        over = True            
    #if diags = X
    if diag1 == ['X','X','X']:
        print('Player X wins!')
        over = True
    if diag2 == ['X','X','X']:
        print('Player X wins!')
        over = True  
    #if one row = O
    length = len(board)-1
    while(length >= 0):
        if board[length] == ['O','O','O']:
            print('Player O wins!')
            over = True
            length -= 1
        else:
            length -= 1
    #if one column = O
    if col1 == ['O','O','O']:
        print('Player O wins!')
        over = True
    if col2 == ['O','O','O']:
        print('Player O wins!')
        over = True
    if col3 == ['O','O','O']:
        print('Player O wins!')
        over = True            
    #if diags = O
    if diag1 == ['O','O','O']:
        print('Player O wins!')
        over = True
    if diag2 == ['O','O','O']:
        print('Player O wins!')
        over = True

    s=''
    s = s.join(board[0]) + s.join(board[1]) + s.join(board[2])
    if(len(s)==9 and over == False):
        print("Scratch Game")
        over = True
def playerInput():
    global playerChar
    global twoPlayer
    position_x, position_y = input("Where do you want to place your move?").split()
    while(len(board[int(position_x)][int(position_y)]) != 0):
        print("Someone has already played there! Try again")
        position_x, position_y = input("Where do you want to place your move?").split()
    board[int(position_x)][int(position_y)] = playerChar
    if playerChar == 'X' and twoPlayer:
        playerChar = 'O'
    elif twoPlayer:
        playerChar = 'X' 
def randomAIinput():
    played = False 
    while(not played):
        position_x = random.randint(0,2)
        position_y = random.randint(0,2)
        if(len(board[position_x][position_y]) == 0):
            board[position_x][position_y] = AIChar
            print("The AI played at " + str(position_x) + ',' + str(position_y))
            played = True
#def minMaxAIinput():
    

def game():
    printBoard()
    endGame()
    while(over == False):
        playerInput()
        printBoard()
        randomAIinput()
        printBoard()
        endGame()


#game()

#So i've decided that I'm going to make a gui for this thing before I make a min max. Then I'll try to find some other 
# AI to play tic tac toe for me.


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = str(board[0][0])
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="left")

        #self.quit = tk.Button(self, text="QUIT", fg="red",
        #                      command=self.master.destroy)
        #self.quit.pack(side="bottom")

        self.hi_there2 = tk.Button(self)
        self.hi_there2["text"] = "-"
        self.hi_there2["command"] = self.say_hi
        self.hi_there2.pack(side="left")

    def say_hi(self):
        #print("hi there, everyone!")
        print(board)
        if(self.hi_there["text"] != 'X'):
            self.hi_there["text"] = 'X'
        else:
            print("You've already played here...")

root = tk.Tk()
app = Application(master=root)
app.mainloop()