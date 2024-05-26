# The great battle of the ships!
This game is based on the classic Battleship game, this time created using Python and runs in the Code Institute mock terminal on Heroku.

The players goal is to find and sink all of the opponents battleships before they find theirs. The opponent in this case is the computer. 

## How to play

The game begins with a short introduction containing the games conditions regarding board size, number of ships and lenght of the ships. 

The player then enters a username and two game boards are generated at random.

The player can only see the ships on their own board, marked with an "S". The computers ships remain hidden. 

There are five ships of various sizes that the player needs to locate in order to win. 

The player will then be asked to guess on the location of the opponents ships via cooordinates on the board, and gets a response in form of a hit or miss.

Hits are marked on the board with an "*", miss with a "X".

The player and the computer take turn in guessing the location of the opponents ships until one of them finds and sinks them all. 

## Features

### Flow chart

### Existing features

* Direct input from "the game" when the user starts, providing some useful information.

* After that the user is asked for input in the form of a username that will appear throughout the game.
A return message in the form of "Oops, not a valid username. Please enter your name again."appears until the player provide us with a valid username - which in this case is one word, letters only. If the user inputs a number, a symbol or more than one word the program will continue ask for a valid one.

* After a correct username is provided a welcome message is returned to the player. The program then print two boards to the game area, paired with a function to randomly place ships on both players boards.

* There is alson a function for hiding the Computers ships on the board from the other player.

* At each new turn the player is asked to input coordinates in a given a row and a column from the provided board size - if the player makes the same guess twice they get a returning message asking for a new guess, until they provide new coordinates. 

* After the player has made their guess the computer gets a shot whch is made randomly, but checks if the coordinates have been hit before and in that case randomly chose another spot to shot at. 

* A function to check after each shot if its a hit or miss, and return a respone to the player.

* A score tracking system that adds a point to the players when they hit the opponents ship.

* After each round the player gets a response about the current score, and are then aksed to either press "Enter" to continue playing, or "q" to quit. If the choose to quit the get a "Thanks for playing!"

* The game continues until one player sinks all the opponents ships. There is a function to check after each round if either the player or the computer has reached the total number of ship cells given in order to win - and if the player wins they get at printed message with a congratulations along with the final score. If the player loose they get a "Better luck next time" along with the final score.


### Features left to implement

* The possibility for the player to position their own ships would be a nice feature, just like when you play the game in real life.

* The option to choose your own board size and the number of ships woud also be a fun feature.  


## Data model eg class

For this project i used the class "Board" for my main functions. I had two classes at one point to keep the features apart, but that only made the programming more complex since the functions I'm using all work together it proved easier to keep most of them in the same class. 


## Testing

I manually tested the program by doing the following:
* Gave invalid input on every place possible - letters instead of numbers, guesses outside of the board size, provided the same guess twice and so on.

* Continuosly tested the run.py in my local terminal and then on the Code Institute Heroku mock terminal.

## Validator testing
I ran the PEP8 Python Validator a few times through out the coding process and fixed the errors as they occured, so that I would not have an enormous list to fix in the end.
* ---No errors were returned from [PEP8 Python Validator](https://pep8ci.herokuapp.com/) in the finished project. Hopefully ...

## Bugs 

There were a LOT of error messages regarding references to functions, arguments, methods and indentations throughout the coding, and Google became my saviour at this point. I've gone through a minimum of 50 error messages while running my program in the local terminal - some of them is visible in my commits, some aren't. But thanks to all the amasing problem solvers in different forums mentioned in the Credit-section, I was hopefully able solve them all. 

### Unsolved bugs


## Deployment
This project was deployed using Code Institutes mock terminal for Heroku
Steps for deployment in Heroku:

The site was deployed to GitHub pages. The steps to deploy are as follows:
In the GitHub repository, navigate to the Settings tab
From the source section drop-down menu, select the Master Branch
Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The link to the mock terminal can be found here - 


## Credits
### Content

Function for

Init section for board class project scope



