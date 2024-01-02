# Emily Ortiz
# January 2023

'''
show user up numbers
roll two dice
tell user what that die returned
check if there is an existing combo
if yes:
    take user innput for numbers they wanna put down
    make sure input is valid numbers
    put down those numbers
    if all numbers down:
        player wins
    else:
        repeat
if no:
    print score
'''

# setup
import math
import random


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
die0 = 0
die1 = 0

# prints remaining numbers
# X represents a "down" number
def display_numbers():
    print("Your numbers: ", end="")
    for number in numbers:
        if number == 0: # 0 represents "down" number
            print("X" + " ", end="")
        else:
            print(str(number) + " ", end="")
    print() # to start a new line

# rolls dice and prints what was rolled
def roll_dice():
    die0 = random.randint(1, 6)
    die1 = random.randint(1, 6)
    total = die0 + die1
    print("You rolled a " + str(total) + "! (" + str(die0) + " + " + str(die1) + ")")

# returns boolean of if game has been won
def check_win():
    for number in numbers:
        if number != 0: # if any numbers aren't down
            return False
    return True

# returns whether numbers attempted to
# be put down is a valid solution for 
# the given roll
def check_valid_solution(tiles, roll):
    num0 = tiles[0]
    num1 = tiles[1]

    # check if numbers are the same
    if num0 == num1:
        print("You cannot lower the same number twice!")
        return False
    # check if numbers are up
    if num0 in numbers and num1 in numbers:
        # check if numbers add up to roll
        if num0 + num1 == roll:
            print("Valid input.")
            return True
        else:
            print("These numbers do not add up to what you rolled!")
            return False
    else:
        print("One or more of these numbers is not available.")
        return False

def main():
    display_numbers()
    roll_dice()

main()