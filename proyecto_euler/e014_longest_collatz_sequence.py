## Plataforma: Project Euler 
## Problem 14: Longest  
## Fecha: 25/08/2025

####### Problem
#The following iterative sequence is defined for the set of positive integers:
#<ul style="list-style-type:none;">
#$n \to n/2$ ($n$ is even)
#$n \to 3n + 1$ ($n$ is odd)
#Using the rule above and starting with $13$, we generate the following sequence:
#$$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$
#It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.
# Project Euler - Problem 14: Longest Collatz Sequence
# Optimizado con memoization (caché)

def collatz_length(n: int, cache: dict[int, int]) -> int:
    """Devuelve la longitud de la cadena de Collatz que inicia en n (incluyendo el 1)."""
    original = n
    path = []

    # Avanza hasta encontrar un valor con longitud conocida en la cache
    while n not in cache:
        path.append(n)
        if n & 1 == 0:       # n es par
            n >>= 1          # n //= 2
        else:                # n es impar
            n = 3 * n + 1

    # Longitud conocida del punto de encuentro
    length = cache[n]

    # Propaga hacia atrás: asigna longitudes a todos los nodos del path
    # (del último al primero para que length vaya creciendo correctamente)
    for v in reversed(path):
        length += 1
        cache[v] = length

    return cache[original]


def longest_collatz_under(limit: int) -> tuple[int, int]:
    """Devuelve (numero_inicial, longitud) con la cadena más larga para números < limit."""
    cache = {1: 1}
    best_n = 1
    best_len = 1

    for i in range(2, limit):
        cur_len = collatz_length(i, cache)
        if cur_len > best_len:
            best_len = cur_len
            best_n = i

    return best_n, best_len


if __name__ == "__main__":
    numero, longitud = longest_collatz_under(1_000_000)
    print(f"Number: {numero}  Steps (terms): {longitud}")

