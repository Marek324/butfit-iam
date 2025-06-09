# Z3 weak planner
# Marek Hric xhricma00

from z3 import *

s = Solver()

employees_count = 9
days_count = 7
shifts_count = 3

X = [ [ (Int("x%s%s1" % (i, j)), Int("x%s%s2" % (i, j))) for j in range(3) ] for i in range(7) ]

employees = list(range(9))

for day in range(7):
    for shift in range(shifts_count):
        # 2 employees on each shift 
        s.add(And(0 <= X[day][shift][0], X[day][shift][0] < 9))
        s.add(And(0 <= X[day][shift][1], X[day][shift][1] < 9))
        s.add(X[day][shift][0] != X[day][shift][1])

# one shift per day per employee
for day in range(7):
    for emp in employees:
        appear = []
        for shift in range(3):
            appear.append(If(X[day][shift][0] == emp, 1, 0))
            appear.append(If(X[day][shift][1] == emp, 1, 0))
        s.add(Sum(appear) <= 1)

if s.check() == sat:
    m = s.model()
    for day in range(days_count):
        print(f"Day {day+1}:")
        for shift in range(shifts_count):
            e1 = m.evaluate(X[day][shift][0])
            e2 = m.evaluate(X[day][shift][1])
            if shift == 0:
                print(f"\tMorning:    {e1}, {e2}")
            elif shift == 1:
                print(f"\tAfternoon:  {e1}, {e2}")
            elif shift == 2:
                print(f"\tNight:      {e1}, {e2}")
else:
    print("UNSAT")
