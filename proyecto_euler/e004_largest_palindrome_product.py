## Plataforma: Project Euler 
## Problema: Largest Palindrome Product
## Fecha: 18/08/2025

###### Problem
## A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.
## Find the largest palindrome made from the product of two $3$-digit numbers.

def is_palindrome(n: int) -> bool:
    rev = 0      # aquí vamos a ir construyendo el número invertido
    x = n        # copia de n para irlo "desarmando"
    while x > 0:
        rev = rev * 10 + (x % 10)
        x //= 10
    return rev == n


max_palindrome = 0
m = 0
# La función range(inicio, fin, paso)
for i in range(999, 99, -1):
    if i * 999 <= max_palindrome:
        break
    for j in range(999, 99, -1):
        m = i * j
        if m < max_palindrome:
            break
        if is_palindrome(m):
            if m > max_palindrome:
                max_palindrome = m
            break
print(max_palindrome)


