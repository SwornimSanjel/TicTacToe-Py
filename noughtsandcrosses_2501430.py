import random
import os.path
import json
random.seed()

def draw_board(board):
    """
    This function draws the game board.
    Displays the board with rows and columns separated by borders using "|" and "-"
    """
    border = " -----------"
    print(border)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print(border)

def welcome(board):
    """
    This function displays a welcome message and initial game board layout.
    It informs the player about the game and shows the current board state.
    Returns draw_board(board) function.
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board layout is shown below:")
    draw_board(board)

def initialise_board(board):
    """
    Initializes the game board with empty cells.
    Also resets the board to its initial empty state for a new round.
    """
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    """
    Prompts the user to select a valid move by showing square for the board
    Checks if the prompted cell is occupied or not.
    Also r.just(27) is used to right justify the string number (eg: 4 5 6) with 27 spaces.
    """
    position_tracking = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    while True:
        print("Choose your square: 1  2  3")
        print("4  5  6".rjust(27))  
        print("7  8  9".rjust(27))
        try:
            position = int(input())
            if position in position_tracking:
                row, column = position_tracking[position]
                if board[row][column] == ' ':
                    return row, column
                else:
                    print("The cell is already occupied. Please try again!")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid inuput. Please enter a number!")

def choose_computer_move(board):
    """
    Chooses a random valid move for the computer using the concept of
    import random module and random.randint().
    
    Selects an empty cell on the board for the computers move.
    """
    while True:
        row, column = random.randint(0,2), random.randint(0,2)
        if board[row][column] == ' ':
            return row, column

def check_for_win(board, mark):
    """
    This function checks if the given mark by player or computer has won the game
    Winning conditions has been initially set so it evaluates to determine the winner.
    """
    conditions_to_win = [
        [board[0][0], board[0][1], board[0][2]], # for top row
        [board[1][0], board[1][1], board[1][2]], # for middle row
        [board[2][0], board[2][1], board[2][2]], # for bottom row
        [board[0][0], board[1][0], board[2][0]], # for left column
        [board[0][1], board[1][1], board[2][1]], # for middle column
        [board[0][2], board[1][2], board[2][2]], # for right column
        [board[0][0], board[1][1], board[2][2]], # for diagonal - top left to bottom right
        [board[0][2], board[1][1], board[2][0]]  # for diagonal - top right to bottom left
    ]
    if [mark, mark, mark] in conditions_to_win:
        return True
    return False

def check_for_draw(board):
    """
    This function checks if the game is a draw or not by evaluating empty cells.
    """
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game(board):
    """
    Initializes, draws the game board and plays the game until there is a win or draw condition.
    Alternates turns between the player and computer to evaluate the winner.
    """
    board = initialise_board(board)
    draw_board(board)
    while True:
        row, column = get_player_move(board)
        board[row][column] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("Congratulations, you win!!")
            return 1
        if check_for_draw(board):
            print("It's a draw match!")
            return 0

        row, column = choose_computer_move(board)
        board[row][column] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins this game!!")
            return -1
        if check_for_draw(board):
            print("It's a draw match!")
            return 0

def menu():
    """
    Displays options to choose for user and returns the players choice.
    Allows the player to choose between playing, saving score, loading scores, or quitting.
    """
    while True:
        print("Enter one of the following options:")
        print("1 - Play the game")
        print("2 - Save score in file 'leaderboard.txt'")
        print("3 - Load and display the scores from the file 'leaderboard.txt'")
        print("q - End the program")
        choice = input("1, 2, 3 or q? ").lower()
        if choice in ["1", "2", "3", "q"]:
            return choice
        else:
            print("Invalid choice. Please try again!")

def load_scores():
    """
    Checks if the file exists or not and loads the leaderboard scores from the file.
    Reads the scores from 'leaderboard.txt' if it exists, otherwise returns an empty dictionary
    """
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            leaders = json.load(file)
    else:
        leaders = {}
    return leaders

def save_score(score):
    """
    Prompts name and saves the players score to the leaderboard file.
    Updates the leaderboard with the players score and writes it to 'leaderboard.txt'.
    """
    name = input("Enter your name for leaderboard: ")
    leaders = load_scores()
    if name in leaders:
        leaders[name] += score  # used to add the score to the existing players name
    else:
        leaders[name] = score  # used to create a new entry for new player name
    with open("leaderboard.txt", "w") as file:
        json.dump(leaders, file)

def display_leaderboard(leaders):
    """
    Displays the leaderboard with player scores.
    Prints the names and scores of all players from the leaderboard.
    """
    print("Leaderboard: ")
    for name, score in leaders.items():
        print(f"{name}: {score}")


