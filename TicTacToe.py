import random
import tkinter as tk
board = [['-','-','-'],['-','-','-'],['-','-','-']]
position_x = 0 
position_y = 0
over = False
playerChar = 'X'
AIChar = 'O'
twoPlayer = False
def endGame():
    global over
    for each in board:
        print(each)
    #TODO check if this method is faster than methods used for columns and diagonals. I would assume it's not. Also I doubt this will be important for this application. 
    #Checks each row if there is a win
    length = len(board)-1
    while(length >= 0):
        if board[length] == ['X','X','X'] or board[length] == ['O','O','O']:
            if board[length][0] == 'X':
                print('Player X wins!')
                over = True
            else:
                print('Player O wins!')
                over = True                
        length -= 1
    #Following block of if statements checks if the corresponding set is a win
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != '-': #Column 1
        print('column 1')
        if board[0][0] == 'X':
            print('Player X wins!')
            over = True
        else:
            print('Player O wins!')
            over = True
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != '-': #Column 2
        print('column 2')
        if board[0][1] == 'X':
            print('Player X wins!')
            over = True
        else:
            print('Player O wins!')
            over = True
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != '-': #Column 3
        print('Column 3')
        if board[0][2] == 'X':
            print('Player X wins!')
            over = True
        else:
            print('Player O wins!')
            over = True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-': #Diagonal 1
        if board[0][0] == 'X':
            print('Player X wins!')
            over = True
        else:
            print('Player O wins!')
            over = True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-': #Diagonal 2
        if board[0][2] == 'X':
            print('Player X wins!')
            over = True
        else:
            print('Player O wins!')
            over = True
    if("-" not in board[0] and "-" not in board[1] and "-" not in board[2] and over == False): #There has to be a cleaner way to do this, but this is functional for now
        print("Scratch Game")
        over = True
def playerInput():
    global playerChar
    global twoPlayer
    position_x, position_y = input("Where do you want to place your move?").split()
    while(board[int(position_x)][int(position_y)] != "-"):
        print("Someone has already played there! Try again")
        position_x, position_y = input("Where do you want to place your move?").split()
    board[int(position_x)][int(position_y)] = playerChar
    if playerChar == 'X' and twoPlayer:
        playerChar = 'O'
    elif twoPlayer:
        playerChar = 'X' 
def randomAIinput():
    #Created this function to get a handle on how the AI would need to input moves. 
    #Interestingly it was incredibly hard to lose or even scratch to this AI. I had to set it to play first so that I could intentionally try and draw the game. 
    played = False 
    while(not played):
        position_x = random.randint(0,2)
        position_y = random.randint(0,2)
        print(position_x, position_y)
        if(board[position_x][position_y] == '-'):
            board[position_x][position_y] = AIChar
            print("The AI played at " + str(position_x) + ',' + str(position_y))
            played = True
#def minMaxAIinput():    

def game():
    endGame()
    while(over == False):
        playerInput()
        endGame()
        if(over):
            break
        randomAIinput()
        endGame()

game()

#So i've decided that I'm going to make a gui for this thing *after* I make a min max. Then I'll try to find some other 
# AI to play tic tac toe for me.


