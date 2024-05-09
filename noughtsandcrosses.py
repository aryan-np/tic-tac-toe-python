import random
import os.path
import json

random.seed()


def draw_board(board):
    # develop code to draw the board
    print(" ----- ----- ----- ")
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(f"|  {board[row][col]}  ", end='')
        print("|\n ----- ----- ----- ")
    pass


def welcome(board):
    # prints the welcome message
    print("welcome")
    # display the board by calling draw_board(board)
    draw_board(board)
    pass


def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = ' '
    return board


def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        try:
            # Ask the user for input
            print(" 1   2   3")
            print(" 4   5   6")
            print(" 7   8   9")
            user_choice = int(input("enter box you wan to choose"))
            if user_choice == 1 or user_choice == 2 or user_choice == 3:
                row = 0
                col = user_choice - 1
            elif user_choice == 4 or user_choice == 5 or user_choice == 6:
                row = 1
                col = user_choice - 4
            elif user_choice == 7 or user_choice == 8 or user_choice == 9:
                row = 2
                col = user_choice - 7
            else:
                print("Please enter valid choice between 1 and 9")

            # Check if the chosen cell is empty
            if board[row][col] == ' ':
                return row, col
            else:
                print("That cell is already occupied. Please choose another.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == mark:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False


def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ':
                return False
    return True


def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # repeat the loop
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            print("user won")
            return 1
        if check_for_draw(board):
            print("draw")
            return 0
        else:
            row, col = choose_computer_move(board)
            board[row][col] = "0"
            draw_board(board)
            if check_for_win(board, "0"):
                print("comp won")
                return -1
            if check_for_draw(board):
                print("draw")
                return 0


def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    # while True:
    print("\t please select an option")
    print("1 - Play the Game")
    print("2 - save score")
    print("3 - display score")
    print("q - exit game")
    choice = (input("enter your choice"))

    return choice


def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    return  # leaders


def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    pass
