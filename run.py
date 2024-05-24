import random
from random import randrange

ships = [2, 3, 3, 4, 5]

class Board:
    """
    Main game board. Creates both players battlefield according to given size,
    placing ships on the boards and handling shots for both player and computer.
    __init__ function created with the help of Project 3 Portfolio Scope.
    """
    def __init__(self, size, num_ships=None, user_name=None):
        self.size = size
        self.num_ships = num_ships
        self.user_name = user_name
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.guesses = set()
        self.ships = set()

    def print_board(self, reveal_ships=False):
        """
        Function for printing the board to the game area.
        Hiding computers ships from the other player with the reveal_ships.
        """
        for row in self.board:
            print(" ".join(['S' if cell == 'S' and reveal_ships else '~' if cell == 'S' else cell for cell in row]))
        print()

    def place_ship(self):
        """
        Function for placing ships on the board. Randomly for each new game.
        """
        for length in ships:
            while True:
                orientation = random.choice(['H', 'V'])
                # H represents horizontal, V represents vertical placement of ships
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                if self.valid_ship_position(row, col, length, orientation):
                    for i in range(length):
                        if orientation == 'H':
                            self.board[row][col + i] = 'S'
                            self.ships.add((row, col + i))
                        else:  # orientation == 'V'
                            self.board[row + i][col] = 'S'
                            self.ships.add((row + i, col))
                    break   

    def valid_ship_position(self, row, col, length, orientation):
        """
        Function for validating the placement of ships at the beginning
        of the game. Making sure no ships overlaps.
        """
        if orientation == 'H' and col + length > self.size:
            return False
        if orientation == 'V' and row + length > self.size:
            return False

        for i in range(length):
            if orientation == 'H' and self.board[row][col + i] != '~':
                    return False
            if orientation == 'H' and self.board[row][col + i] != '~':
                    return False
        return True
    
    def handle_shot(self, row, col):
        """
        Handle a shot at the given position and return whether it was a hit or miss.
        """
        if (row, col) in self.guesses:
            return "Oh, you've already shot here!"
        self.guesses.add((row, col))
        if (row, col) in self.ships:
            self.board[row][col] = '*'
            self.ships.remove((row, col))
            return "That was a hit!"
        else:
            self.board[row][col] = 'X'
            return "That was a miss."

    def sunk_all_ships(self):
        """
        Check if all ships have been hit.
        """
        return len(self.ships) == 0


class Battleship:
    """
    This class contains functions for handling both players shots.
    It also contains the function for getting a username from the player.
    """
    def get_player_shot(self, size):
            """
            Get the player's shot and validate the input from the player.
            If input is invalid it loops to ask for new input from player.
            """
            while True:
                try:
                    row = int(input(f"Guess a row (0 to {size - 1}): "))
                    col = int(input(f"Guess a column (0 to {size - 1}):"))
                    if 0 <= row < size and 0 <= col < size:
                        return row, col
                    else:
                        print(f"Invalid input. Please enter numbers within the range 0 to {size - 1}.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    return self.get_player_shot(size)


    def get_computer_shot(self, size, previous_shots):
        """
        Generate a random shot for the computer.
        Learned about randint from the Project Portfolio Scope.
        """
        while True:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            if (row, col) not in previous_shots:
                previous_shots.add((row, col))
                return row, col            


    def get_username(self):
        """
        Function for getting players name and thus creating a username.
        Contains validation for correct input.
        """
        print("Let's start by adding a username")
        print("Username must be one word, letters only.")
        while True:
            user_name = input("Please enter your name here: \n")
            print()
            if user_name.isalpha():
                print(f"Hello and welcome {user_name}, now let the battle begin!\n")
                return user_name
            else:
                print("Oops, not a valid username. Please enter your name again.")


def new_game():
    size = 6
    num_ships = 5
    player_score = 0
    computer_score = 0
    battleship = Battleship()
    print("========================================\n")
    print("Welcome to the great Battle of the ships!")
    print("Board size: 6x6. Number of ships: 5.")
    print("Size of ships vary from 2-5 spaces.")
    print("Top left corner is row 0, col 0\n")
    print("========================================\n")
    user_name = battleship.get_username()
    print("========================================\n")

    # Create battlefields for player and computer
    player_board = Board(size)
    computer_board = Board(size)

    # Place ships for the player and computer
    player_board.place_ship()
    computer_board.place_ship()

    computer_shots = set()    

    #Main playing loop
    while True:
        # Print player's battlefield
        print(f"{user_name}'s battlefield:")
        player_board.print_board(reveal_ships=True)
        # Print computer's visible battlefield
        print("Computer's battlefield:")
        computer_board.print_board(reveal_ships=False)

        # Players turn
        print("Take a shot at your opponent's battlefield:")
        row, col = battleship.get_player_shot(size)
        result = computer_board.handle_shot(row, col)
        print(f"Player guessed ({row}, {col}) and {result}")
        if result == "That was a hit!":
            player_score +=1

        # Computers turn
        row, col = battleship.get_computer_shot(size, computer_shots)
        result = player_board.handle_shot(row, col)
        print(f"Computer shot at ({row}, {col}) and {result}\n")
        if result == "That was a hit!":
            computer_score +=1    

        #Print scores after each round
        print("After this round, the scores are:")
        print(f"{user_name}: {player_score}")
        print(f"Computer: {computer_score}\n")
        cont = input("Press 'Enter' to continue, or 'q' to quit\n")
        if cont == 'q':
            print("========================================\n")
            print("Thanks for playing!\n")
            break


        """
        Check if all ships are hit and announce the winner.
        sum() adds up the lenght of all the ships to see who reaches it first - which in this case is 17.
        """
        if player_score == sum(lenght for lenght in ships) or computer_score == sum(lenght for lenght in ships):
            break
            
        if player_score > computer_score:
            print(f"Congratulations {user_name}!, you sunk all your opponents ships!")
        else:
            print(f"Oh no the computer won! Better luck next time.")
            
        print(f"Final score: Player {player_score}, Computer {computer_score}")    
        print("========================================\n")


new_game()
