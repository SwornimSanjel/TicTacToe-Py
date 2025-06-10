from noughtsandcrosses_2501430 import *

def main():
    """
    This is the main function to execute the "Unbeatable Noughts and Crosses game"
    
    Initializes the game board and handles the games main menu.
    According to the players choice, it plays the game, saves and
    loads score from leaderboard and ends the program.
    """
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
        ]

    welcome(board)
    total_score = 0  # initialising the initial score
    while True:
        choice = menu()
        if choice == "1":
            score = play_game(board)
            total_score += score
            print("Your current score is:", total_score)
        elif choice == "2":
            save_score(total_score)
            total_score = 0
        elif choice == "3":
            leader_board = load_scores()
            display_leaderboard(leader_board)
        elif choice == "q":
            print("Thank you for playing the 'Unbeatable Noughts and Crosses' game.")
            print("Good Bye")
            return


if __name__ == '__main__':
    """
    Checks if the script is executed directly.
    If the script is run directly it calls the main function to start the game.
    """
    main()
            
