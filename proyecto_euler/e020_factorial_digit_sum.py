## Plataforma: Project Euler 
## Problem 20: Factorial Digit Sum 
## Fecha: 20/08/2025

###### Problem
## n! means n * (n - 1) ... * 1
## For example, $10! = 10 \times 9 \times \cdots \times 3 \times 2 \times 1 = 3628800$,<br>and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.
## Find the sum of the digits in the number $100!$.


def sum_digit(n: int) -> int:
    total_sum = 0
    
    while n > 0:
        total_sum += n % 10
        n = n // 10

    return total_sum 

def factorial(n: int) -> int:
    if n > 1:
        return n * factorial(n-1)
    else:
        return n



print( sum_digit( factorial(10) ) )
print( sum_digit( factorial(100) ) )

