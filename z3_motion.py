# Z3 calculation of motion equation
# Marek Hric xhricma00

# Brouk Kvapník přijíždí k semaforu rychlostí 25.0 m/s.
# Rozsvítí se žlutá, a Brouk šlápne na brzdu a smykem zabrzdí.
# Pokud je Broukovo zrychlení je -9.00 m/s2, jakou vzdálenost auto ujede? 

from z3 import *

velf = Real('vf')
veli = Real('vi')
acc = Real('a')
time = Real('t')
dist = Real('d')

s = Solver()

s.add(velf == 0)
s.add(veli == 25.0)
s.add(acc == -9.0)
s.add(dist == (veli*time) + (acc * time**2) / 2)
s.add(velf == veli + acc * time)

if s.check() == sat:
    print(f"Distance: {s.model()[dist]}m")
else:
    print("UNSAT")
