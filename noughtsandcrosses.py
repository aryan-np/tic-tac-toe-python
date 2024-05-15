import random
import os.path
import json
random.seed()


def draw_board(board):
    """
        Draws the tic-tac-toe board.

        Parameters::
        board : list of (marks and empty space in board)
            The current state of the board, where each cell is represented by a string.

        Returns::
        None
        """
    print(" ----- ----- ----- ")
    for row in range(3):
        for col in range(3):
            print(f"|  {board[row][col]}  ", end='')
        print("|\n ----- ----- ----- ")


def welcome(board):
    """
    Welcomes the player and displays the initial board.

    Parameters::
    board : list of (marks and empty space in board)
        The initial empty board.

    Returns::
    None
    """
    print(" *** welcome to noughts and crosses game by Aryan *** ")
    draw_board(board)


def initialise_board(board):
    """
     Initializes the board to an empty state.

     Parameters:
     
     board : list of (marks and empty space in board)
         The board to be initialized.

     Returns:
     
     board : list of marks and empty space in board
         The initialized board with all cells set to ' '.
     """
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = ' '
    return board


def get_player_move(board):
    """
      Prompts the player to make a move.

      Parameters:
      
      board : list of (marks and empty space in board)
          The current state of the board.

      Returns:
      
      tuple of int
          The row and column of the player's chosen move.
      """
    while True:
        try:
            print(" 1 | 2 | 3")
            print(" 4 | 5 | 6")
            print(" 7 | 8 | 9")
            user_choice = int(input("enter box you want to choose \nEnter Your Choice >>> "))
            if 1 <= user_choice <= 9:
                user_choice -= 1
                row = user_choice // 3
                col = user_choice % 3
            else:
                print("*** ERROR *** \n Please enter valid choice between 1 and 9")
                continue

            # Check if the chosen cell is empty
            if board[row][col] == ' ':
                return row, col
            else:
                print("*** ERROR *** \nThat cell is already occupied. Please choose another.")
        except ValueError:
            print("*** ERROR *** \nInvalid input. Please enter a number.")


def choose_computer_move(board):
    """
       Randomly chooses a move for the computer.

       Parameters:
       
       board : list of marks and empty space in board
           The current state of the board.

       Returns:
       
       tuple of int
           The row and column of the computer's chosen move.
       """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col


def check_for_win(board, mark):
    """
        Checks if the specified mark has won the game.

        Parameters:
        
        board : list of marks and empty space in board
            The current state of the board.
        mark : str
            The mark to check for a win ('X' or 'O').

        Returns:
        
        bool
            True if the specified mark has won, False otherwise.
        """
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
    """
       Checks if the game is a draw.

       Parameters:
       
       board : list of marks and empty space in board
           The current state of the board.

       Returns:
       
       bool
           True if the game is a draw, False otherwise.
       """
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ':
                return False
    return True


def play_game(board):
    """
        Plays a game of tic-tac-toe.

        Parameters:
        
        board : list of marks and empty space in board
            The current state of the board.

        Returns:
        
        int
            1 if the player wins, -1 if the computer wins, 0 if the game is a draw.
        """
    comp_mark = "\033[93m" + "O" + "\033[0m"
    user_mark = "\033[94m" + "X" + "\033[0m"
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = user_mark
        draw_board(board)
        if check_for_win(board, user_mark):
            print("*** Congratulations! You Won ***")
            return 1
        if check_for_draw(board):
            print("*** its a draw *** ")
            return 0
        else:
            row, col = choose_computer_move(board)
            board[row][col] = comp_mark
            draw_board(board)
            if check_for_win(board, comp_mark):
                print("*** Sorry You Lost computer won the match *** ")
                return -1
            if check_for_draw(board):
                print("*** its a draw *** ")
                return 0


def menu():
    """
      Displays the main menu and prompts the user to select an option.

      Returns:
      
      str
          The user's choice from the menu options.
      """
    print(" *** please select an option *** ")
    print("1 - Play the Game")
    print("2 - save score")
    print("3 - display score")
    print("q - exit game")
    choice = (input("Enter your choice \nEnter your choice >>> "))
    if choice not in "123q":
        print("*** Please enter a valid option ***")

    return choice


def load_scores():
    """
       Loads the leaderboard from a file.

       Returns:
       
       dict
           A dictionary containing the leaderboard.
       """
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
    """
        Saves the player's score to the leaderboard.

        Parameters:
        
        score : int
            The player's score to be saved.

        Returns:
        
        None
        """
    while True:
        name = input("Enter your name: (do not leave blank)")
        if name != "":
            break

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
    if name in leaders.keys():
        leaders[name] += score
    else:
        leaders[name] = score
    leaders = dict(sorted(leaders.items(), key=lambda key_value_tuple: key_value_tuple[1], reverse=True))
    # Save leaderboard to file
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)


def display_leaderboard(leaders):
    """
        Displays the leaderboard.

        Parameters:
        
        leaders : dict
            A dictionary containing the leaderboard.

        Returns:
        
        None
        """
    print("Leaderboard:")
    for name, score in leaders.items():
        print(f"{name}: {score}")
