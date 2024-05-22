class Board:
    """
    Main board. Creates both players battlefield according to given size, placing ships on the boards 
    and handling players shots. __init__ function created with the help of Project 3 Portfolio Scope.
    """
    def __init__(self, size, num_ships, user_name):
        self.size = size
        self.num_ships = num_ships
        self.user_name = user_name
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.guesses = []
        self.ships = []

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
    print("========================================\n")
    print("Welcome to the great Battle of the ships!")
    print("Board size: 6x6. Numb of ships: 5.")
    print("Top left corner is row 0, col 0\n")
    print("========================================\n")
    user_name = get_username()  
    print("========================================\n")

main()               