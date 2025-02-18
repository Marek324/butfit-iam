# IAM bonus task - sudoku
# Author: Marek Hric xhricma00

import sys
from itertools import combinations

def encode(x, y, v):
    return 100*x + 10*y + v

def invalidate_unused_vars():
    clauses = []
    for x in range(10):
        for y in range(10):
            for v in range(10):
                if x + y + v == 0:
                    continue
                if encode(x, y, v) < 111 or encode(x, y, v) % 10 == 0:
                    clauses.append([-encode(x, y, v)])
    return clauses

def parse_input(clauses):
    for line in sys.stdin:
        row, col, val = map(int, line.strip().split())
        
        if 0 <= row > 9 or 0 <= col > 9 or 0 <= val > 9:
            print("Invalid input", file=sys.stderr)
            sys.exit(1)

        clauses.append([encode(row, col, val)])
    return clauses

def at_least_one_in_cell(row, col):
    vars = [encode(row, col, val) for val in range(1,10)]
    return [vars]

def at_most_one_in_row(row, val):
    vars = [encode(row, y, val) for y in range(1,10)]
    result = []
    comb = list(combinations(vars, 2))
    for c in comb:
        result.append([-c[0], -c[1]])
    return result

def at_most_one_in_column(col, val):
    vars = [encode(x, col, val) for x in range(1,10)]
    result = []
    comb = list(combinations(vars, 2))
    for c in comb:
        result.append([-c[0], -c[1]])
    return result

def at_most_one_in_block(x, y, v):
    """
    x, y - coordinates of the block [0,0] - [2,2]
    v - value
    """
    vars = [encode(x*3+i, y*3+j, v) for i in range(1,4) for j in range(1,4)]
    result = []
    comb = list(combinations(vars, 2))
    for c in comb:
        result.append([-c[0], -c[1]])
    return result

def clauses_to_string(clauses):
    string = ""
    for clause in clauses:
        string += " ".join(map(str, clause)) + " 0\n"
    return string

if __name__ == "__main__":
    cnf_formula = ""
    clauses = invalidate_unused_vars()
    variables = 999

    clauses += parse_input(clauses)

    for i in range(1,10):
        for j in range(1,10):
            clauses += at_most_one_in_row(i, j)
            clauses += at_most_one_in_column(i, j)
            clauses += at_least_one_in_cell(i, j)
    
    for i in range(3):
        for j in range(3):
            for v in range(1,10):
                clauses += at_most_one_in_block(i, j, v)

    cnf_formula += f"p cnf {variables} {len(clauses)}\n"
    cnf_formula += clauses_to_string(clauses)
    print(cnf_formula)
    