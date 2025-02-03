import random

def play():
    c = 1
    name = str(input("Hello! What's your name?\n"))
    n = random.randint(1,20)
    number = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n"))
    while number != n:
        c += 1
        if number < n:
            number = int(input("Your guess is too low.\nTake a guess\n"))
        elif number > n:
            number = int(input("Your guess is too high.\nTake a guess\n"))

    print(f"Good job, {name}! You guessed my number in {c} guesses!")
