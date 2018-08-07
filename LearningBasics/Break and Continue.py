import random

magicNumber = random.randint(1, 100)

for i in range(101):
    if i == magicNumber:
        print(i, "is the magic number! Awesome!")
        break
    else:
        print(i)

numbersTaken = [2, 5, 11, 12, 19]

print("Here are the numbers that are still available:")

for i in range(1, 21):
    if i in numbersTaken:
        continue
# continue stops the loop at this current point and restarts it
    print(i)
