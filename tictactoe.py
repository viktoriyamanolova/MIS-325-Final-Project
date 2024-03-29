# Tic Tac Toe Game

import random
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inpPlayerLetter():
    letter = ''
    while not (letter == 'R' or letter == 'J'):
        print('\nWould you like to be R or J? \n')
        letter = input().upper()
    if letter == 'R':
        return ['R', 'J']
    else:
        return ['J', 'R']

def firstPlayer():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Would you like to play again? (yes or no) \n')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def freeSpace(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(board, int(move)):
        print('\nWhere would you like to move next? (1-9) \n')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if freeSpace(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'R':
        playerLetter = 'J'
    else:
        playerLetter = 'R'
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if freeSpace(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if freeSpace(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if freeSpace(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if freeSpace(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inpPlayerLetter()
    turn = firstPlayer()
    print('\nThe ' + turn + ' will go first.\n')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('\nCongratulations! You won the game! \n')
                gameIsPlaying = False
                
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('\nThe game is a tie! \n')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('\nSorry! You lost the game! \n')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('\nThe game is a tie! \n')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break
        