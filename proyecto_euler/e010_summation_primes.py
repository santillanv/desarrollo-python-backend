## Plataforma: Project Euler 
## Problem 10: Summation of Primes 
## Fecha: 20/08/2025

###### Problem
## The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.
## Find the sum of all the primes below two million.</p>

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


sum_prime = 2 ## El primer primo es 2
i = 3         ## Se inicia en 3 porque ningun par edespues de dos es primo 
target = 2_000_000

while i < target:
    if is_prime(i):
        sum_prime += i
    i += 2

print(sum_prime)

