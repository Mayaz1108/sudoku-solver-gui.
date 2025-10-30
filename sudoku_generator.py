import random
from sudoku_solver import solve_sudoku, is_valid

def generate_full_board():
    board = [[0]*9 for _ in range(9)]
    numbers = list(range(1, 10))
    for i in range(9):
        random.shuffle(numbers)
        for j in range(9):
            board[i][j] = numbers[j]
            if not is_valid(board, i, j, board[i][j]) or not solve_sudoku(board):
                board[i][j] = 0
    solve_sudoku(board)
    return board

def remove_cells(board, difficulty='medium'):
    holes = {'easy': 35, 'medium': 45, 'hard': 55}[difficulty]
    while holes > 0:
        i, j = random.randint(0, 8), random.randint(0, 8)
        if board[i][j] != 0:
            board[i][j] = 0
            holes -= 1
    return board
