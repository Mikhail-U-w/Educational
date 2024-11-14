numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
checker = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
for i in numbers:
    amount = 0
    for n in checker:
        well = i % n
        if well == 0:
            amount = amount + 1
        if i < n:
            break
    if amount > 1:
        Not_Primes.append(i)
    else:
        Primes.append(i)
Primes.remove(1)
print('Primes: ', Primes)
print('Not_Primes: ', Not_Primes)