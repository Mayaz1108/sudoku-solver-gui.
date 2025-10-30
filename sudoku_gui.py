import tkinter as tk
from tkinter import messagebox
from sudoku_solver import solve_sudoku
from sudoku_generator import generate_full_board, remove_cells

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.difficulty = tk.StringVar(value='medium') # Default difficulty
        master.title("Sudoku Solver & Generator")

        self.board = [[0]*9 for _ in range(9)]
        self.entries = [[None]*9 for _ in range(9)]

        frame = tk.Frame(master, bg="black")
        frame.grid(row=0, column=0, padx=10, pady=10)

        for i in range(9):
            for j in range(9):
                color = "gray" if (i // 3 + j // 3) % 2 == 0 else "white"

                entry = tk.Entry(
                    frame, width=2, font=('Arial', 20), justify='center',
                    bg=color, relief='flat', highlightthickness=1,
                    highlightbackground='black'
                )

                entry.grid(row=i, column=j)
                self.entries[i][j] = entry

        # Control Buttons
        btn_frame = tk.Frame(master)
        btn_frame.grid(row=1, column=0, pady=10)

        tk.Button(btn_frame, text="Generate", command=self.generate_puzzle, width=10).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Solve", command=self.solve_puzzle, width=10).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear_board, width=10).grid(row=0, column=2, padx=5)

        # Add difficulty selection
        tk.OptionMenu(btn_frame, self.difficulty, 'Easy', 'Medium', 'Hard').grid(row=0, column=3, padx=5)

    def read_board(self):
        """Reads the matrix from the GUI entries"""
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                self.board[i][j] = int(val) if val.isdigit() else 0

    def display_board(self):
        """Displays the board"""
        for i in range(9):
            for j in range(9):
                val = self.board[i][j]
                self.entries[i][j].delete(0, tk.END)
                if val != 0:
                    self.entries[i][j].insert(0, str(val))

    def solve_puzzle(self):
        self.read_board()
        if solve_sudoku(self.board):
            self.display_board()
            messagebox.showinfo("Sudoku", "Puzzle Solved!")
        else:
            messagebox.showwarning("Sudoku", "No solution found.")

    def generate_puzzle(self):
        self.board = generate_full_board()
        self.board = remove_cells(self.board, difficulty=self.difficulty.get())
        self.display_board()

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
        self.board = [[0]*9 for _ in range(9)]


if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
