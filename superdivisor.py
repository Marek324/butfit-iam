import sys
import math

def super_divisor(n):
    if n == 0 or n == 1:
        return 0
    for i in range(math.floor(n/2), 0, -1):
        if n % i == 0:
            return i
    return 1

def main(n):
    solutions = []
    for i in range(2, n + 1):
        current = i
        sum_val = current
        
        while current > 1:
            current = super_divisor(current)
            sum_val += current
            
            if sum_val > n:
                break
        
        if sum_val == n:
            solutions.append(i)

    if len(solutions) == 0:
        print("No solutions")
        return

    for sol in solutions:
        print(sol)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        main(n)
    else:
        print("Please provide a number as a command line argument")
