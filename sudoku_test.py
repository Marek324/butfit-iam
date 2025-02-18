import sys

def decode(v):
    x = v // 100
    v %= 100
    y = v // 10
    v %= 10
    return x, y, v

def create_sudoku_grid(solution):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for cell in solution:
        if cell > 0:
            x, y, v = decode(cell)
            grid[x-1][y-1] = v 

    return grid

def check_sudoku(grid):
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            if grid[i][j] in row or grid[j][i] in col:
                return False
            row.add(grid[i][j])
            col.add(grid[j][i])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = set()
            for x in range(3):
                for y in range(3):
                    if grid[i + x][j + y] in square:
                        return False
                    square.add(grid[i + x][j + y])

    return True

def print_grid(grid):
    horizontal = "─"
    vertical = "│"
    cross = "┼"
    horizontal_d = "═"
    vertical_d = "║"
    cross_d = "╬"

    row_sep = (horizontal * 3 + cross) * 2 + horizontal * 3 + vertical_d + (horizontal * 3 + cross) * 2 + horizontal * 3 + vertical_d + (horizontal * 3 + cross) * 2 + horizontal * 3
    thick_row_sep = ((horizontal_d * 4) * 2 + horizontal_d * 3 + cross_d) * 2 + (horizontal_d * 4) * 2 + horizontal_d * 3

    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print(thick_row_sep)
        elif i != 0:
            print(row_sep)

        print(" ", end="") 
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(f" {vertical_d}", end=" ")
            elif j != 0:
                print(f" {vertical}", end=" ")
            print(f"{num}", end="")
        print()

if __name__ == "__main__":
    isSat = sys.stdin.readline() == "SAT\n"
    if not isSat:
        print("Unsatisfiable")
        sys.exit(0)

    solution = sys.stdin.readline().split()
    grid = create_sudoku_grid(list(map(int, solution)))
    valid = check_sudoku(grid)
    print_grid(grid)
    print("Valid" if valid else "Invalid")