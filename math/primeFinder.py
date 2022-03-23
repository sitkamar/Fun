max = input("Enter the max number: ")
primes = []
for i in range(2, int(max)):
    isPrime = True
    for p in primes:
        if i % p == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
print(primes)