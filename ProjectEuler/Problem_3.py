def isPrime(y):
    for i in range(2, y):
        if y % i == 0:
            return False
    return True


def isFactor(n, y):
    if n % y == 0:
        return True
    return False


n = 600851475143

for y in range(2, n):
    if isPrime(y):
        if isFactor(n, y):
            print(y)

