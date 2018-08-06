def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def isFactor(n, x):
    if n % x == 0:
        return True
    return False


n = 600851475143

for x in range(2, n):
    if isPrime(x):
        if isFactor(n, x):
            print(x)

