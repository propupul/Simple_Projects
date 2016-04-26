import random

__author__ = "Proupul"

# Guess the number - Computer things of a number between 1 and 100
# The user has to guess which number it is.
# After every guess the computer tells the user to go higher or lower.
# Until the guess is correct.

print("Welcome! The computer will guess a number between 1 and 100")
print("The computer will tell you if your guess is higher or lower")

# start_num = int(input("Please chose the starting number: "))
# end_num = int(input("Please chose the ending number: "))

random_num = random.randint(1, 100)

counter = 1
keep_going = 'y'
while keep_going == 'y':
    guess = int(input("I'm thinking of a number between",
                      "1 and 100 guess it: "))
    if guess != random_num:
        counter += 1
    else:
        counter = counter
    if guess > random_num:
        print("You need to go lower!")
    elif guess < random_num:
        print("You need to go higher")
    else:
        print("You got it! It took you", counter, "tries to get the answer")
        keep_going = input("Would you like to continue? [y/n]: ")
