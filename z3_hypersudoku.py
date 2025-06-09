# Z3 hypersudoku solver
# Marek Hric xhricma00

from z3 import *

M = [ [ Int("x%s%s" % (i+1, j+1)) for j in range(9) ]
      for i in range(9) ]

# cell contains a value
cell = [ And(1 <= M[i][j], M[i][j] <= 9)
             for i in range(9) for j in range(9) ]

# once in row
row = [ Distinct(M[i]) for i in range(9) ]

# once in column
col = [ Distinct([ M[i][j] for i in range(9) ])
            for j in range(9) ]

# once in box
box = [ Distinct([ M[3*i0 + i][3*j0 + j]
            for i in range(3) for j in range(3) ])
            for i0 in range(3) for j0 in range(3) ]

# once in hyperblock
hblock = [ Distinct([ M[i0 + i][j0 + j]
            for i in range(3) for j in range(3)])      
            for (i0,j0) in [(1,1),(1,5),(5,1),(5,5)]]

# all constraints together
hsudoku = cell + row + col + box + hblock

I =((0,0,6, 0,0,0, 2,0,3),
    (0,5,0, 0,0,7, 1,0,4),
    (0,0,1, 3,2,0, 0,6,0),
    
    (6,0,0, 0,0,0, 0,5,0),
    (0,0,5, 8,0,0, 0,0,0),
    (0,0,8, 0,5,0, 4,0,0),
    
    (0,0,7, 0,0,0, 0,0,0),
    (9,0,0, 5,0,0, 0,0,1),
    (0,2,0, 0,0,0, 0,0,0))

inst = [ If(I[i][j] == 0, True,
                  M[i][j] == I[i][j])
               for i in range(9) for j in range(9) ]

s = Solver()
s.add(hsudoku + inst)
if s.check() == sat:
    m = s.model()
    print_matrix([ [ m.evaluate(M[i][j]) for j in range(9) ] for i in range(9) ])
else:
    print ("failed to solve")
