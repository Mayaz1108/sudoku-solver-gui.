# Sudoku Solver and Generator (with GUI)

A complete Sudoku project implemented in **Python**, combining
algorithmic logic (**Backtracking & Recursion**) with a clean **Tkinter GUI**.

This project demonstrates how to solve and generate Sudoku puzzles
programmatically while providing an interactive visual interface.

---

## Features
- **Automatic Solver** — Solves any valid Sudoku using recursive backtracking.
- **Board Generator** — Creates random Sudoku puzzles by difficulty (`easy`, `medium`, `hard`).
- **Graphical Interface** — Play or visualize solutions using Tkinter.
- **Algorithmic Focus** — Showcases recursion, constraint checking, and logic.
- **Lightweight** — Pure Python, no external dependencies.

---

## Project Structure
```
sudoku-solver-gui/
├── main.py              # Console interface: generate + solve Sudoku
├── sudoku_solver.py     # Core solver logic (backtracking algorithm)
├── sudoku_generator.py  # Board creation + difficulty adjustment
├── sudoku_gui.py        # Tkinter GUI interface (buttons + grid)
└── README.md            # Project documentation
```

---

## How to Run

### Option 1 – Run the GUI version
```bash
python sudoku_gui.py
```

### Option 2 – Run the console version
```bash
python main.py
```

---

## Algorithm Overview
### Sudoku Solver
1. Finds the next empty cell (marked as 0).
2. Tries placing numbers 1–9.
3. Checks if each move is valid:
   - Not repeated in the same row.
   - Not repeated in the same column.
   - Not repeated in the same 3×3 block.
4. If valid, continues recursively.
5. If stuck, backtracks to the previous cell.

### Sudoku Generator
1. Fills a full, valid Sudoku board using the solver.
2. Randomly removes cells to create a puzzle.
3. The number of removed cells depends on the difficulty level.

---

## Example GUI
<img width="546" height="667" alt="image" src="https://github.com/user-attachments/assets/9781b3eb-362b-4be3-a665-abfdb645c872" />
---

## Requirements
Built with **Python 3.x** and standard libraries only:
- `tkinter`
- `random`

No installation required.

---

## Author
**Maya Zeevi**  
A computer science student project combining algorithmic thinking with practical GUI programming.

---

## License
This project is licensed under the **MIT License** — feel free to use, modify, and share.
