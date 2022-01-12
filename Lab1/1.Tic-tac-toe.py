global aiMove1
global aiMove2
global ai
global ai2
global board

def delay() :
    for i in range(0, 10) :
        for j in range(0, 100) :
            pass

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' ----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("\n")


def spaceFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("DRAW!")
            exit()
        if checkWin():
            if letter == ai:
                print("AI ALGORITHM WINS! BETTER LUCK NEXT TIME!")
                exit()
            else:
                print("HURRAY! YOU WIN!")
                exit()

        return


    else:
        print("Can't place your symbol there. Position already occupied!")
        position = int(input("Please enter new position : "))
        insertLetter(letter, position)
        return


def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichSymbolWon(symbol):
    if board[1] == board[2] and board[1] == board[3] and board[1] == symbol:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == symbol):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == symbol):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == symbol):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == symbol):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == symbol):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == symbol):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == symbol):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def compMove2():
    print("AI Algorithm 2 thinking...")
    delay()
    bestScore = 999
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = ai2
            score = algorithm(board, 0, True)
            board[key] = ' '
            if (score < bestScore):
                bestScore = score
                bestMove = key

    insertLetter(ai2, bestMove)
    return



def compMove1():
    print("AI Algorithm 1 thinking...")
    delay()
    bestScore = -999
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = ai
            score = algorithm(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(ai, bestMove)
    return


def algorithm(board, depth, isMaximizing):
    if (checkWhichSymbolWon(ai)):
        return 1
    elif (checkWhichSymbolWon(ai2)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -999
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = ai
                score = algorithm(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 999
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = ai2
                score = algorithm(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)
print("You are playing Tic-Tac-Toe against the AI Algorithm! Good luck.")
print("Positions on the board are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
print("You can either play as X or O")
ai2 = input("Make choice for Algorithm 2 now. Enter X or O : ")
while(True) :
    if ai2 == "X" or ai2 == "x" :
        ai = "O"
        ai2 = "X"
        aiMove1 = False
        aiMove2 = True
        break
    elif ai2 == "O" or ai2 == "o" :
        ai = "X"
        ai2 = "O"
        aiMove1 = True
        aiMove2 = False
        break
    else :
        print("Please enter either X or O correctly!")
        exit()

while not checkWin():
    if ai == "X" :
        delay()
        compMove1()
        compMove2()
        
    else :
        delay()     
        compMove2()
        compMove1()