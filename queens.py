# IAM task 1
# Author: Marek Hric xhricma00

import sys
from itertools import combinations

def encode(i, j, n):
    return i * n + j + 1

def at_least_one(i, n, orientation):
    if orientation == "row":
        vars = [encode(i, j, n) for j in range(n)]
    else:
        vars = [encode(j, i, n) for j in range(n)]
    
    return [vars]

def at_most_one(i, n, orientation):

    if orientation == "row":
        vars = [encode(i, j, n) for j in range(n)]
    else:
        vars = [encode(j, i, n) for j in range(n)]

    
    result = []
    comb = list(combinations(vars, 2))
    
    for c in comb:
        result.append([-c[0], -c[1]])
        
    
    return result


def diagonal(i, n, orientation):
    if i == 0:
        return []
    

    if orientation == "major_top":
        vars = range(i, (n**2 - (i - 1) * n + 1), n + 1)
    elif orientation == "major_left":
        vars = range((i * n) + 1, n**2 - (i - 1) , n + 1)
    elif orientation == "minor_top":
        vars = range(i+1, i*n+2, n - 1)
    elif orientation == "minor_right":
        vars = range(i * n, n**2, n - 1)


    result = []
    comb = list(combinations(vars, 2))
    
    for c in comb:
        result.append([-c[0], -c[1]])

    
    return result


if __name__ == "__main__":

    if(len(sys.argv) != 2):
        print("Usage: python3 queens.py <n>")
        sys.exit(1)


    n = int(sys.argv[1])
    if n < 1:
        print("N must be at least 1")
        sys.exit(1)


    clauses = []
    # One variable for each cell
    variables = n**2

    for i in range(n):        
        clauses += at_least_one(i, n, "row")
        clauses += at_least_one(i, n, "col")

        clauses += at_most_one(i, n, "row")
        clauses += at_most_one(i, n, "col")

        clauses += diagonal(i, n, "major_top")
        clauses += diagonal(i, n, "major_left")
        clauses += diagonal(i, n, "minor_right")
        if i != n-1:
            clauses += diagonal(i, n, "minor_top")


    print("p cnf", variables, len(clauses))
    for c in clauses:
        print(" ".join(map(str, c)), "0")
