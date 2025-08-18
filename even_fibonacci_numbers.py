## Problema: Even Fibonacci Numbers
## Plataforma: Project Euler 
## Fecha: 17 Agosto 2025
def sum_even_fib_fast(limit: int = 4_000_000) -> int:
    a, b = 2, 8       # E1, E2
    total = 0
    while a <= limit:
        total += a
        a, b = b, 4*b + a   # siguiente par: E_{n} = 4E_{n-1} + E_{n-2}
    return total

if __name__ == "__main__":
    print("Suma:", sum_even_fib_fast())



