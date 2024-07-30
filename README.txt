# Tic Tac Toe Game

## Created by Owen Campbell

### Description

This is a simple command-line Tic Tac Toe game implemented in Python. The game allows a human player to compete against a computer player, which makes random moves. The game board is displayed in a 3x3 grid format, and the player can choose their move by entering a number between 0 and 8 corresponding to the board position.

### Files

- `main.py`: The main script containing the game logic and classes.

### Classes

#### Board

This class represents the Tic Tac Toe game board.

- `__init__(self)`: Initializes the board with 9 empty spaces.
- `display(self)`: Displays the current state of the board.
- `check_win(self, symbol)`: Checks if the given symbol ('X' or 'O') has a winning combination.
- `check_draw(self)`: Checks if the game is a draw.
- `check_is_ongoing(self)`: Checks if the game is still ongoing.

#### Player

This class represents a player in the Tic Tac Toe game.

- `__init__(self, symbol)`: Initializes the player with a given symbol ('X' or 'O').
- `make_move(self, game_board, position)`: Allows the player to make a move at the specified position on the game board.
- `make_random_move(self, game_board)`: Makes a random move on the game board.

### Functions

#### main()

The main function runs the game loop, which includes:

1. Initializing the game board and players.
2. Alternating turns between the human player and the computer player.
3. Displaying the game board after each move.
4. Checking for a win, draw, or ongoing game after each move.
5. Prompting the player to play again after the game ends.

### How to Run

1. Ensure you have Python installed on your system.
2. Save the code to a file named `main.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where `main.py` is saved.
5. Run the script using the command: `python main.py`.

### Gameplay Instructions

1. When prompted, enter a number between 0 and 8 to make your move. The numbers correspond to the board positions as follows:

0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8

2. The computer will make a random move after your turn.
3. The game will display the current board state after each move.
4. The game will announce the winner or if it's a draw after the game ends.
5. You can choose to play again or exit the game when prompted.

### Example

Enter your move (0-8): 4
 X |   |  
---------
 O | X | O 
---------
   |   | X

Player X wins!
Do you want to play again? (y/n): n

Enjoy playing Tic Tac Toe!
