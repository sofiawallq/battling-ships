

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
    get_username()  

main()               