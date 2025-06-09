# Z3 proof of De Morgan's Laws
# Marek Hric xhricma00

from z3 import *

x = Bool('x')
y = Bool('y')
s = Solver()

# De Morgan's Laws
# 1. Not (A and B) is equivalent to (Not A) or (Not B)
l1l = Not(And(x, y))
l1r = Or(Not(x), Not(y))

# proof by contradiction
s.add(l1l != l1r)
if s.check() == unsat:
    print("De Morgan's Law 1 is valid")
else:
    print("De Morgan's Law 1 is not valid")


# 2. Not (A or B) is equivalent to (Not A) and (Not B)
l2l = Not(Or(x, y))
l2r = And(Not(x), Not(y))

# proof by contradiction
s.add(l2l != l2r)
if s.check() == unsat:
    print("De Morgan's Law 2 is valid")
else:
    print("De Morgan's Law 2 is not valid")
