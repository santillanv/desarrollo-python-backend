## Plataforma: Project Euler 
## Problem 12: Highly Divisible Triangular Number
## https://projecteuler.net/problem=12
## Date: 28/08/2025  7503531

def triangle_number (n: int) -> int:
    return (n*(n+1)) // 2

def count_divisors(n: int) -> int:
    divisors = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors += 2 if i != n // i else 1
        i += 1
    return divisors


#for i in range (1,15,1):
#    print("i: ",i," Triangle number: ",triangle_number(i), " Divisors: ",count_divisors(i))

target = 500
flag = True
i = 500
while flag:
    i += 1
    tn = triangle_number(i)
    cd = count_divisors(tn)
#    print("i: ",i," Triangle number: ",tn, " Divisors: ",cd)
    if cd > target:
        print(triangle_number(i))
        flag = False
