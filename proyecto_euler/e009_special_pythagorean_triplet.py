## Plataforma: Project Euler 
## Problem 9: Special Pythagorean Triplet
## Fecha: 19/08/2025

###### Problem
## A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
## a^2 + b^2 = c^2
## For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.
## There exists exactly one Pythagorean triplet for which a + b + c = 1000 Find the product abc
## -------------------------

def special_triplet_sum_1000():
    target = 1000
    # a < b < c  ⇒  a como mucho 332 y b < (1000 - a)/2
    for a in range(1, target // 3):                     # a < 333
        for b in range(a + 1, (target - a) // 2):       # b < c ⇒ b < (1000-a)/2
            c = target - a - b                          # evita el tercer bucle
            if a*a + b*b == c*c:
                print("Triplete:", a, b, c)
                print("Producto:", a*b*c)
                return a, b, c, a*b*c                   # SALE inmediatamente
    return None

print(special_triplet_sum_1000())
