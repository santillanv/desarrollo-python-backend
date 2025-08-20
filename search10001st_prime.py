## Plataforma: Project Euler 
## Problem 7: 10 001st Prime
## Fecha: 19/08/2025

###### Problem
## By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.
## What is the $10\,001$st prime number?

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    max_divisor = int (n ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

prime = 1
i = 3 
search = 10001

while prime < search:
    if is_prime(i):
        prime += 1
    if prime == search:
        break
    i += 2

print(i)

