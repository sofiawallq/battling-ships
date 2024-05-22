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