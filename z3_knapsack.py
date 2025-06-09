# Z3 knapsack problem solver
# Marek Hric xhricma00

from z3 import *

N = 24
C = 6404180

s = Solver()

Bag = [
    (3, 4), (4, 5), (5, 7), (1, 3), (7, 10), (8, 11), (2, 3), (5, 8), (6, 9), (4, 6),
    (3, 5), (2, 4), (7, 25), (1, 1), (5, 15), (3, 7), (4, 12), (6, 14), (9, 18), (7, 13),
    (3, 6), (5, 9), (8, 17), (4, 8), (2, 3), (6, 11), (5, 10), (3, 4), (7, 16), (9, 20),
    (2, 2), (1, 1), (4, 9), (6, 13), (8, 15), (5, 12), (3, 5), (4, 6), (7, 14), (2, 3),
    (6, 10), (5, 8), (3, 5), (8, 19), (4, 7), (2, 3), (7, 12), (9, 21), (5, 9), (3, 4)
]

# list of variables for each item
x = [Bool(f'x{i}') for i in range(len(Bag))]

#If(condition, true, false)
s.add(Sum([If(x[i], Bag[i][0], 0) for i in range(len(Bag))]) <= N)
s.add(Sum([If(x[i], Bag[i][1], 0) for i in range(len(Bag))]) == C)

def print_bag(model, bag):
    for item in range(len(bag)):
        if model.evaluate(x[item]):
            print("Added with weight " + str(bag[item][0]) + " and cost " + str(bag[item][1]))

if s.check() == sat:
    m = s.model()
    print_bag(m, Bag)
else:
    print("Failed to solve")
