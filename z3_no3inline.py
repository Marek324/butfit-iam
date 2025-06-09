# Z3 no 3 in line problem solver
# Marek Hric xhricma00 

from z3 import *

N = 10
points = 20 
s = Solver()

X = [ [ Int("x%s%s" % (i+1, j+1)) for j in range(N) ]for i in range(N) ]

for i in range(N):
    for j in range(N):
        s.add(Or (X[i][j] == 0, X[i][j] == 1))
        
# at most 2 in row
for i in range(N):
    s.add(Sum([X[i][j] for j in range(N)]) <= 2)

# at most 2 in column
for j in range(N):
    s.add(Sum([X[i][j] for i in range(N)]) <= 2)

# at most 2 in diagonal
for i in range(N):
    for j in range(N):
        diagonal_left = []
        diagonal_right = []
        k, l, m = i, j, j
        while k < N and l < N:
            diagonal_left.append(X[k][l])
            diagonal_right.append(X[k][m])
            k, l, m = k + 1, l + 1, m - 1
        s.add(Sum(diagonal_left) <= 2)
        s.add(Sum(diagonal_right) <= 2)

s.add(Sum([X[i][j] for i in range(N) for j in range(N)]) == points)

if s.check() == sat:
    m = s.model()
    counter = 0
    for i in range(N):
        print([m.evaluate(X[i][j]) for j in range(N)])
else:
    print("UNSAT")
