import sys

def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def prime_domain(d):
    primes = []
    for i in range(2, d):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def possible_solutions(d1, d2):
    r1_dom = prime_domain(d1)
    r2_dom = prime_domain(d2)
    d = gcd(d1, d2)
    sols = []
    
    for r1 in r1_dom:
        for r2 in r2_dom:
            if (r1 - r2) % d == 0:
                sols.append((r1, r2))
    
    return sols

def dividends(n, d1, d2):
    sols = []
    possible = possible_solutions(d1, d2)

    for r1, r2 in possible:
        x = d2 * n + r2 - r1
        divisor = d1 + d2
        
        if x % divisor != 0:
            continue
        q1 = x // divisor
        q2 = n - q1
        
        if q1 < 0 or q2 < 0:
            continue
        
        x = d1 * q1 + r1
        sols.append(x)

    return sols


def main(n, d1, d2):
    solutions = dividends(n, d1, d2)

    if len(solutions) == 0:
        print("No solution")
        return

    for sol in solutions:
        print(sol)

if __name__ == '__main__':
    n = int(sys.argv[1])
    d1 = int(sys.argv[2])
    d2 = int(sys.argv[3])
    main(n, d1, d2)
