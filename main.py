# Created by Owen Campbell
import random

class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
    
    def display(self):
        for row in range(3):
            print("|".join(self.board[row * 3:(row + 1) * 3]))
            if row < 2:
                print("-----")
                
    def check_win(self, symbol):
        win_scenarios = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_scenarios:
            if all(self.board[i] == symbol for i in condition):
                return True
        return False
    
    def check_draw(self):
        return ' ' not in self.board
    
    def check_is_ongoing(self):
        return ' ' in self.board and not self.check_win('X') and not self.check_win('O')
            
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def make_move(self, game_board, position):
        if game_board.board[position] == ' ':
            game_board.board[position] = self.symbol
        else:
            print("Position is taken. Try again!")
    
    def make_random_move(self, game_board):
        empty_positions = [i for i, spot in enumerate(game_board.board) if spot == ' ']
        if empty_positions:
            position = random.choice(empty_positions)
            game_board.board[position] = self.symbol

def main():
    while True:
        board = Board()
        player1 = Player('X')
        player2 = Player('O')
        current_player = player1
        
        while board.check_is_ongoing():
            board.display()
            if current_player == player1:
                try:
                    position = int(input("Enter your move (0-8): "))
                    if position < 0 or position > 8:
                        raise ValueError
                    if board.board[position] != ' ':
                        print("Position is taken. Try again!")
                        continue
                    current_player.make_move(board, position)
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 8.")
                    continue
            else:
                current_player.make_random_move(board)
            
            if board.check_win(current_player.symbol):
                board.display()
                print(f"Player {current_player.symbol} wins!")
                break
            
            if board.check_draw():
                board.display()
                print("It's a draw!")
                break
            
            current_player = player2 if current_player == player1 else player1

        if input("Do you want to play again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()