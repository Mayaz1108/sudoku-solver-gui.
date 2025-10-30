from sudoku_generator import generate_full_board, remove_cells
from sudoku_solver import solve_sudoku

def print_board(board):
    for i in range(9):
        print(" ".join(str(x or ".") for x in board[i]))

if __name__ == "__main__":
    difficulty = 'medium'  # Can be 'easy', 'medium', or 'hard'
    board = generate_full_board()
    puzzle = remove_cells(board, difficulty='medium')
    print(f"Sudoku Puzzle, Level: {difficulty.capitalize()}\n")
    print_board(puzzle)

    print("\nSolving...\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
