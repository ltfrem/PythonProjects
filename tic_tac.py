import sys

#Initialize all squares to be empty
board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}
board_keys = []
for key in board:
    board_keys.append(key)
    
#Function for printing board after each move
def print_board(board):
    print('|' + board['1'] + '|' + board['2'] + '|' + board['3'] + '|')
    print('|' + board['4'] + '|' + board['5'] + '|' + board['6'] + '|')
    print('|' + board['7'] + '|' + board['8'] + '|' + board['9'] + '|')

#Function to test for a restart
def restart():
    restart = input("Would you like to play again? (y/n)")
    if restart.lower() == 'y':
        for key in board:
            board[key] = ' ' #Turn all spaces back to blank
        game('X')
    else:
        sys.exit('Goodbye')

#Function for the gameplay
def game(turn):
    count = 0
    for i in range(50):
        print_board(board)
        print("It's your turn, " + turn + ". Which space would you like to play?")
        print("1 = top left, 2 = top middle, 3 = top right,\n4 = middle left, 5 = middle,"
              " 6 = middle right,\n7 = bottom left, 8 = bottom middle, 9 = bottom right")
        try:
            move = input()
            if board[move] == ' ':
                board[move] = turn
                count += 1
            else:
                print("That space is already filled. Pick another space to play.\n")
                continue
        except KeyError: #If user's entry is not 1-9
            print("Sorry, your entry is invalid. Please pick a space to play.\n")
            continue
        
        #Check if anyone has won
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ': #Across the bottom
                print_board(board)
                print("Game Over. " + turn + " won.")
                break
            elif board['4'] == board['5'] == board['6'] != ' ': #Across the middle
                print_board(board)
                print("Game Over. " + turn + " won.")
                break
            elif board['1'] == board['2'] == board['3'] != ' ': #Across the top
                print_board(board)
                print("Game Over. " + turn + " won.")
                break
            elif board['1'] == board['4'] == board['7'] != ' ': #Down the left side
                print_board(board)
                print("Game Over. " + turn + " won.")
                break
            elif board['2'] == board['5'] == board['8'] != ' ': #Down the middle
                print_board(board)
                print("Game Over. " + turn + " won.")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': #Down the right side
                print_board(board)
                print("Game Over. " + turn + " won.")
                break
            elif board['7'] == board['5'] == board['3'] != ' ': #Diagonal
                print_board(board)
                print("Game Over. " + turn + " won.")
                break
            elif board['1'] == board['5'] == board['9'] != ' ': #Diagonal
                print_board(board)
                print("Game Over. " + turn + " won.")
                break
        
        #Check for a tie
        if count == 9:
            for i in board:
                if board[i] == ' ':
                    continue
                else:
                    print_board(board)
                    print("Game Over. Game is a draw.")
                    restart()
        
        #Change player after each move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    #Do they want to play again?
    restart()
game('X') #Start the game, X goes first