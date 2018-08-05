n = int(input())

for x in range(n):
    print(pow(x, 2))

while n < 20:
    print("n is not big enough: " + str(n))
    n += 1
