print("WELCOME TO ONLINEGAMES.COM")

import random
import time

choice = input("Choose from the following games\n1. Number Guesser\n2. Lottery Game")

# Number Guessing Game
if choice == "1" or choice == "Number Guesser":
    print("Welcome to the number guessing game")
    print("Guess what number between 1 and 20")
    number = int(input("Guess:"))
    computer = random.randint(1, 35)
    turns = 4
    goes = 0

    while number:
        if number != computer and number > computer:
            print("Number is lower")
            turns -= 1
            goes += 1
            print(turns, "goes remaining")
            number = int(input("Guess:"))

        if number != computer and number < computer:
            print("Number is higher")
            turns -= 1
            goes += 1
            print(turns, "goes remaining")
            number = int(input("Guess:"))
        if number == computer:
            print("You got it in", goes, "tries")
            break
        if turns == 0:
            print("Out of tries, Game Over")
            break

# Lottery Game

if choice == "2" or choice == "Lottery Game":
    print("Welcome to Lottery Online")
    print("Pick 7 numbers")
    count = 10
    n1 = int(input("1st pick"))
    n2 = int(input("2nd pick"))
    n3 = int(input("3rd pick"))
    n4 = int(input("4th pick"))
    n5 = int(input("5th pick"))
    n6 = int(input("6th pick"))
    n7 = int(input("7th pick"))

    l1 = random.randint(1, 35)
    l2 = random.randint(1, 35)
    l3 = random.randint(1, 35)
    l4 = random.randint(1, 35)
    l5 = random.randint(1, 35)
    l6 = random.randint(1, 35)
    l7 = random.randint(1, 35)

    print("Good Luck")

    while count != 0:
        print(count)
        count -= 1
        time.sleep(0.5)

    print("Your numbers:", n1, n2, n3, n4, n5, n6, n7)
    print("Winning numbers:", l1, l2, l3, l4, l5, l6, l7)