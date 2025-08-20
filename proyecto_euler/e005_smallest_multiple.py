## Plataforma: Project Euler 
## Problema 5: Smallest Multiple
## Fecha: 18/08/2025

###### Problem
## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple(n: int) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19]  # primos ≤ 20
    result = 1
    for p in primes:
        k = 1
        while p**(k+1) <= n:
            k += 1
        result *= p**k
    return result

print(smallest_multiple(20))

