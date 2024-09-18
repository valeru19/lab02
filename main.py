def sieve_of_eratosthenes(limit):
    """Возвращает список простых чисел до заданного предела с использованием решета Эратосфена."""
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

if __name__ == "__main__":
    # Пример использования
    n = int(input("Введите предел для поиска простых чисел: "))
    primes = sieve_of_eratosthenes(n)
    print(f"Простые числа до {n}: {primes}")
