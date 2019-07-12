# a4.py
import random

def initBoard():
    array = []
    for i in range(9):
        array.append(".")
    return array

def currBoard(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    
def numBoard(state):
    array = []
    for index,data in enumerate(state):

        if data=='.':
            array.append(index+1)
        else:
            array.append(" ")

    print(array[0], array[1], array[2])
    print(array[3], array[4], array[5])
    print(array[6], array[7], array[8])

def checkGame(state):
    #return 0 game incomplete/tie, 1 human win, 2 comp win
    # Computer wins Row
    if state[0]=='X' and state[1]=='X' and state[2]=='X':
        return 2
    if state[3]=='X' and state[4]=='X' and state[5]=='X':
        return 2
    if state[6]=='X' and state[7]=='X' and state[8]=='X':
        return 2
    # Computer wins Column
    if state[0]=='X' and state[3]=='X' and state[6]=='X':
        return 2
    if state[1]=='X' and state[4]=='X' and state[7]=='X':
        return 2
    if state[2]=='X' and state[5]=='X' and state[8]=='X':
        return 2
    # Computer wins Diagonal
    if state[0]=='X' and state[4]=='X' and state[8]=='X':
        return 2
    if state[2]=='X' and state[4]=='X' and state[6]=='X':
        return 2
    # User wins Row
    if state[0]=='O' and state[1]=='O' and state[2]=='O':
        return 1
    if state[3]=='O' and state[4]=='O' and state[5]=='O':
        return 1
    if state[6]=='O' and state[7]=='O' and state[8]=='O':
        return 1
    # Computer wins Column
    if state[0]=='O' and state[3]=='O' and state[6]=='O':
        return 1
    if state[1]=='O' and state[4]=='O' and state[7]=='O':
        return 1
    if state[2]=='O' and state[5]=='O' and state[8]=='O':
        return 1
    # Computer wins Diagonal
    if state[0]=='O' and state[4]=='O' and state[8]=='O':
        return 1
    if state[2]=='O' and state[4]=='O' and state[6]=='O':
        return 1
    
    return 0

# Moves available
def availMoves(state):
    array=[]
    for i,d in enumerate(state):
        if d=='.':
            array.append(i+1)
    return array

# Make move human
def humanMove(state, num):
    num=int(num)-1
    state[num] = 'O'
    return state   

# Make move computer
def compMove(state, num):
    num=int(num)-1
    state[num] = 'X'
    return state 

# simulate game to completion
def MCTS(state, numRemain):
    prob = {}
    
    #number of random moves
    for i in range(200):
        option = availMoves(state)
        curstate = state.copy()
        choose = int(random.choice(option))
        curstate = compMove(curstate, choose)
        if choose not in prob:
            prob[choose]=0
        numRemain2=numRemain
        #completing the game

        while numRemain2 > 0:
            if checkGame(curstate)==2:
                prob[choose] = prob[choose]+1
                break
            #human move
            option = availMoves(curstate)
            choose2 = int(random.choice(option))
            curstate = humanMove(curstate, choose2)
            numRemain2 = numRemain2-1

          
            if checkGame(curstate)==1:
                prob[choose] = prob[choose]-1
                break

            #comp move
            if numRemain2 > 0:
                option = availMoves(curstate)
                choose2 = int(random.choice(option))
                curstate = compMove(curstate, choose2)
        if checkGame(curstate)==0 and numRemain2==0:
                prob[choose] = prob[choose]+1
                
    return max(prob, key=prob.get)

##Main Code
if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe. Computer is X and you are O. Let's Play.")
    print("")
    board = initBoard()
    currBoard(board)
    print("")
    numBoard(board)
    option = availMoves(board)
    choose = int(random.choice(option))
    board = compMove(board, choose)
    print("Computer choose move: ",choose)
    currBoard(board)
    print("")
    numBoard(board)

    for i in range(4,0,-1):
        move = input("Please type available move above: ")
        board = humanMove(board, move)
        currBoard(board)
        print("")
        numBoard(board)
        if checkGame(board) == 1:
            print("User Won")
            break

        

        print("")
        newMove = MCTS(board,i-1 )
        print("Computer choose move :", newMove)
        board = compMove (board, newMove)
        currBoard(board)
        print("")
        numBoard(board)
        if checkGame(board) == 2:
            print("Computer Won")
            break

        if checkGame(board) == 0 and i==1:
            print("Tie")
            break
        
        

    
