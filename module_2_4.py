numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for k in numbers:
    if k == 1:
        continue
    is_prime = True

    for i in range(2, k):
        if k % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(k)
    else:
        not_primes.append(k)

print("Простые числа:", primes)
print("Не простые числа:", not_primes)