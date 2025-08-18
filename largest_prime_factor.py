## Problema: Largest Prime Factor
## Plataforma: Project Euler 
## Fecha: 17/08/2025
###### Problem
## The prime factors of 13195 are 5, 7, 13 and 29
## What is the largest prime factor of the number 600851475143

def largest_prime_factor(n: int) -> int:
    max_p = None

    # quita todos los 2
    while n % 2 == 0:
        max_p = 2
        n //= 2

    # prueba solo impares
    i = 3
    while i * i <= n:
        while n % i == 0:
            max_p = i
            n //= i
        i += 2

    # si queda un primo grande > 1, es el mayor
    if n > 1:
        max_p = n

    return max_p

print(largest_prime_factor(600851475143))  # 6857
