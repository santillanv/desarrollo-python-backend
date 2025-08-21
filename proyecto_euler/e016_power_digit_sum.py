## Plataforma: Project Euler 
## Problem 16: Power Digit Sum 
## Fecha: 20/08/2025

###### Problem
## 2^{15} = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
## What is the sum of the digits of the number $2^{1000}
def sum_digit(n: int) -> int:
    total_sum = 0
    
    while n > 0:
        total_sum += n % 10
        n = n // 10

    return total_sum 

print(sum_digit(2**1000))

