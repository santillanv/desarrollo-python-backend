## Plataforma: Project Euler 
## Problema 6: Sum Square Difference
## Fecha: 19/08/2025

###### Problem
# The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385.$$
# The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares(n: int) -> int:
    result = 0

    for i in range(n):
        result += (i + 1) * (i + 1)
        
    return result

def squares_sum(n: int) -> int:
    result = 0 
    for i in range(n):
        result += i + 1 
    return result * result

a = squares_sum(100)
b = sum_squares(100)


print(a -b)
