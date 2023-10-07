import tkinter as tk

def solve(puzzle):
    find = find_empty(puzzle)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(puzzle, num, (row, col)):
            puzzle[row][col] = num

            if solve(puzzle):
                return True
            puzzle[row][col] = 0
    return False

def is_valid(puzzle, num, pos):
    for i in range(len(puzzle[0])):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(puzzle)):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == num and (i, j) != pos:
                return False
    return True

def find_empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return i, j
    return None

def solve_sudoku_gui():
    input_puzzle = [[int(entries[i][j].get()) for j in range(9)] for i in range(9)]
    if is_valid_sudoku(input_puzzle):
        solve(input_puzzle)
        update_gui(input_puzzle)
    else:
        output_label.config(text="Not a valid Sudoku.")

def is_valid_sudoku(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0 and (puzzle[i].count(puzzle[i][j]) > 1 or
                                      [puzzle[x][j] for x in range(9)].count(puzzle[i][j]) > 1):
                return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [puzzle[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            subgrid = [x for x in subgrid if x != 0]
            if len(subgrid) != len(set(subgrid)):
                return False

    return True

def update_gui(puzzle):
    for i in range(9):
        for j in range(9):
            cell_value = puzzle[i][j]
            if cell_value != 0:
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(cell_value))
            else:
                entries[i][j].delete(0, tk.END)

# Initialize the GUI
root = tk.Tk()
root.title("Sudoku Solver")

# Create entry widgets for input Sudoku
entries = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j] = tk.Entry(root, font=('Arial', 24), width=2, justify="center")
        entries[i][j].grid(row=i, column=j)

# Create a button to solve the Sudoku
solve_button = tk.Button(root, text="Solve Sudoku", command=solve_sudoku_gui)
solve_button.grid(row=10, column=0, columnspan=9, pady=10)

# Create an output label for messages
output_label = tk.Label(root, font=('Arial', 16))
output_label.grid(row=11, column=0, columnspan=9, pady=10)

# Run the GUI event loop
root.mainloop()
