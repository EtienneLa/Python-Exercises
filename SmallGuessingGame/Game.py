import random

rnd_number = random.randint(1, 10)
tries = 1

user = input("Welcome, what is your name? ")

confirm = input("Hello " + user + ". Let's play a game? [y/n] ")
if confirm == "n":
    print("kkbb.")
    exit()
if confirm == "y":
    print("I am thinking of a number between 1 & 10.")
    guess = int(input("Have a guess: "))
while guess != rnd_number:
    if guess < rnd_number:
        print("Higher!")
    if guess > rnd_number:
        print("Lower!")
    tries += 1
    guess = int(input("Try again: "))
if guess == rnd_number:
    str_num = str(rnd_number)
    str_tries = str(tries)
    print("Congrats, the number was " + str_num + ", indeed! It took you " + str_tries + " tries.")
