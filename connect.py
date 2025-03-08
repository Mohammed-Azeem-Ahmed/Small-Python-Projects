class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'  # Player 1 uses 'X', Player 2 uses 'O'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 13)
        print('0 1 2 3 4 5 6')

    def make_move(self, col):
        if col < 0 or col > 6 or self.board[0][col] != ' ':
            return False  # Invalid move

        for row in reversed(self.board):
            if row[col] == ' ':
                row[col] = self.current_player
                return True
        return False  # Column is full

    def check_winner(self):
        # Check horizontal
        for row in self.board:
            for col in range(4):
                if row[col] == self.current_player and all(row[col + i] == self.current_player for i in range(4)):
                    return True

        # Check vertical
        for col in range(7):
            for row in range(3):
                if self.board[row][col] == self.current_player and all(self.board[row + i][col] == self.current_player for i in range(4)):
                    return True

        # Check / diagonal
        for row in range(3, 6):
            for col in range(4):
                if self.board[row][col] == self.current_player and all(self.board[row - i][col + i] == self.current_player for i in range(4)):
                    return True

        # Check \ diagonal
        for row in range(3, 6):
            for col in range(3, 7):
                if self.board[row][col] == self.current_player and all(self.board[row - i][col - i] == self.current_player for i in range(4)):
                    return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            self.print_board()
            col = int(input(f"Player {self.current_player}, choose a column (0-6): "))
            if self.make_move(col):
                if self.check_winner():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                self.switch_player()
            else:
                print("Invalid move, try again.")

if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()
