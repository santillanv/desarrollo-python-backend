## Plataforma: Project Euler 
## Problem 12: Highly Divisible Triangular Number
## https://projecteuler.net/problem=12
## Date: 28/08/2025  7503531

def build_spf(limit: int):
    """Devuelve arreglo SPF (smallest prime factor) para 0..limit."""
    spf = list(range(limit + 1))
    for i in range(2, int((limit) ** 0.5) + 1):
        if spf[i] == i:
            step = i
            start = i * i
            for j in range(start, limit + 1, step):
                if spf[j] == j:
                    spf[j] = i
    return spf

def count_divisors_spf(n: int, spf) -> int:
    """Cuenta divisores usando SPF."""
    if n == 1:
        return 1
    d = 1
    x = n
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        d *= (e + 1)
    return d

def divs_of_triangular_spf(n: int, spf, cache: dict) -> int:
    if n % 2 == 0:
        a = n // 2
        b = n + 1
    else:
        a = n
        b = (n + 1) // 2
    da = cache.get(a)
    if da is None:
        da = count_divisors_spf(a, spf)
        cache[a] = da
    db = cache.get(b)
    if db is None:
        db = count_divisors_spf(b, spf)
        cache[b] = db
    return da * db

def first_triangular_with_divs_over_spf(threshold: int):
    # Límite: suficiente para factorizar los 'a' y 'b' (n y n+1)/2 del primer T_n > threshold.
    # 2_000_000 va holgado y corre muy rápido en Python.
    limit = 2_000_000
    spf = build_spf(limit)
    cache = {}
    n = 1
    while True:
        d = divs_of_triangular_spf(n, spf, cache)
        if d > threshold:
            return n, (n * (n + 1)) // 2, d
        n += 1

if __name__ == "__main__":
    n, t, d = first_triangular_with_divs_over_spf(500)  # luego sube a 500
    print(f"n={n}, T_n={t}, divisores={d}")

