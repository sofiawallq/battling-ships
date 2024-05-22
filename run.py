import random 
from random import randrange

class Board:
    """
    Main board. Creates both players battlefield according to given size, placing ships on the boards 
    and handling players shots. __init__ function created with the help of Project 3 Portfolio Scope.
    """
    def __init__(self, size, num_ships=None, user_name=None):
        self.size = size
        self.num_ships = num_ships
        self.user_name = user_name
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.guesses = []
        self.ships = []

    def create_battlefield(self, reveal_ships=False):
        """
        Function for printing the board to the game area.
        Hiding computers ships from the other player with the reveal_ships.
        """
        for row in self.board:
            if reveal_ships:
                print(" ".join(row))
            else:
                print(" ".join(['S' if cell == 'S' else cell for cell in row]))
        print()    

    def valid_ship_position(self, row, col, length, orientation):
            """
            Function for validating the placement of ships at the beginning of the game.
            Making sure no ships overlaps.
            """
            if orientation == 'H':
                if col + length > self.size:
                    return False
                for i in range(length):
                    if self.board[row][col + i] != '~':
                        return False
            else:  # orientation == 'V'
                if row + length > self.size:
                    return False
                for i in range(length):
                    if self.board[row + i][col] != '~':
                        return False
            return True 

    def place_ship(self, length):
        """
        Function for placing ships on the board.
        """
        placed = False 
        while not placed:
            orientation = random.choice(['H', 'V'])
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.valid_ship_position(row, col, length, orientation):
                if orientation == 'H':
                    for i in range(length):
                        self.board[row][col + i] = 'S'
                        self.ships.append((row, col + i))
                else:  # orientation == 'V'
                    for i in range(length):
                        self.board[row + i][col] = 'S'
                        self.ships.append((row + i, col))
                placed = True   


def get_username():
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
            print(f"Hello and welcome {user_name}, let the battle begin!\n")
            return user_name
        else:
            print("Oops, not a valid username. Please enter your name again.")  

def main():
    size = 6
    num_ships = 5
    ships = [2, 3, 3, 4, 5]
    print("========================================\n")
    print("Welcome to the great Battle of the ships!")
    print("Board size: 6x6. Numb of ships: 5.")
    print("Size of ships vary from 2-5 spaces.")
    print("Top left corner is row 0, col 0\n")
    print("========================================\n")
    user_name = get_username()  
    print("========================================\n")

    # Create battlefields for player and computer
    player_board = Board(size)
    computer_board = Board(size)

    # Place ships for the player and computer
    for ship_length in ships:
        player_board.place_ship(ship_length)
        computer_board.place_ship(ship_length)

    # Print player's battlefield
    print(f"{user_name}'s battlefield:")
    player_board.create_battlefield(reveal_ships=True)
    # Print computer's visible battlefield
    print("Computer's battlefield:")
    computer_board.create_battlefield(reveal_ships=False)   
    
main()               