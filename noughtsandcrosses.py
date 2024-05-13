import random
import os.path
import json

random.seed()


def draw_board(board):
    print(" ----- ----- ----- ")
    for row in range(3):
        for col in range(3):
            print(f"|  {board[row][col]}  ", end='')
        print("|\n ----- ----- ----- ")


def welcome(board):
    print("welcome")
    draw_board(board)


def initialise_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = ' '
    return board


def get_player_move(board):
    while True:
        try:

            print(" 1   2   3")
            print(" 4   5   6")
            print(" 7   8   9")
            user_choice = int(input("enter box you wan to choose"))
            if 1 <= user_choice <= 9:
                user_choice -= 1
                row = user_choice // 3
                col = user_choice % 3
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
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col


def check_for_win(board, mark):
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
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ':
                return False
    return True


def play_game(board):
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
    print("\t please select an option")
    print("1 - Play the Game")
    print("2 - save score")
    print("3 - display score")
    print("q - exit game")
    choice = (input("enter your choice"))

    return choice


def load_scores():
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            try:
                leaders = json.load(file)
            except json.JSONDecodeError:
                leaders = {}  # Return an empty dictionary if the file is empty or not valid JSON
    else:
        leaders = {}
    return leaders


def save_score(score):
    name = input("Enter your name: ")

    # Load existing leaderboard if it exists
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            try:
                leaders = json.load(file)
            except json.JSONDecodeError:
                leaders = {}  # Return an empty dictionary if the file is empty or not valid JSON
    else:
        leaders = {}  # Create an empty dictionary if the file doesn't exist

    # Update leaderboard with current player's score
    leaders[name] = score

    # Save leaderboard to file
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)


def display_leaderboard(leaders):
    print("Leaderboard:")
    for name, score in leaders.items():
        print(f"{name}: {score}")

