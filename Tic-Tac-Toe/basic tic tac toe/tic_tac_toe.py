import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        # Create a frame for the game board
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        # Create game board
        self.board = [None] * 9
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.frame, text="", width=5, height=2, font=('Arial', 24),
                               command=lambda x=i: self.play(x))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        # Set up game state
        self.player = "X"
        self.winner = None
        self.game_over = False

        # Create a label to show the status
        self.status_label = tk.Label(master, text="Current Player: X", font=('Arial', 16))
        self.status_label.pack(pady=10)

    def play(self, position):
        if self.board[position] is None and not self.game_over:
            self.board[position] = self.player
            self.buttons[position].config(text=self.player)
            self.check_winner()
            if not self.game_over:
                self.player = "O" if self.player == "X" else "X"
                self.status_label.config(text=f"Current Player: {self.player}")

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] is not None:
                self.game_over = True
                self.winner = self.board[i]
                self.highlight_winner(i, i + 1, i + 2)
                return

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] is not None:
                self.game_over = True
                self.winner = self.board[i]
                self.highlight_winner(i, i + 3, i + 6)
                return

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] is not None:
            self.game_over = True
            self.winner = self.board[0]
            self.highlight_winner(0, 4, 8)
            return
        if self.board[2] == self.board[4] == self.board[6] is not None:
            self.game_over = True
            self.winner = self.board[2]
            self.highlight_winner(2, 4, 6)
            return

        # Check for tie
        if None not in self.board:
            self.game_over = True
            self.status_label.config(text="It's a Tie!")

    def highlight_winner(self, *positions):
        for pos in positions:
            self.buttons[pos].config(bg="yellow")
        self.status_label.config(text=f"Player {self.winner} Wins!")

# Create the main window
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()