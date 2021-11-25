# ex11.py
"""
    * write a lift off program using a for loop

    * Given a list of alphabets, from a - z , 
    use a loop to print out the vowels 
    ( Tips: list of vowels, loop, condition )

    * Write a program that simulates the rolling of a dice.
    A fair dice has 6 sides numbered from 1 to 6.
    Take an integer input from the user as the number of 
    times the dice must be rolled and this value must be 
    greater than 50.

    Using a loop ( any loop ) and an if , elif 
    and else statement ( if necessary) and then
     print the number of times a particular number 
    was obtained when the dice was rolled.
"""


# write a lift off program using a for loop

from random import randint
print("lift of in ")
for i in range(5):
    if i < 4:
        print(i, end=", ")
    else:
        print(i)

print("Good job!!")
print()


# Given a list of alphabets, from a - z , use a loop to print out the vowels

alphabets = [
    "a", "b", "c", "d",
    "e", "f", "g", "h",
    "i", "j", "k", "l",
    "m", "n", "o", "p",
    "q", "r", "s", "t",
    "u", "v", "w", "x",
    "y", "z"
]

vowels = ["a", "e", "i", "o", "u"]

for letter in alphabets:
    if letter in vowels:
        print(letter)

print()


# a program that simulates the rolling of a dice


# the fair dices have values
# 1 2 3 4 5 6 which has indices of
# 0 1 2 3 4 5 in the simulation result respectively
# another approach would be to use a dictionary
simulation_result = [0, 0, 0, 0, 0, 0]


try:
    number_of_simulations = int(
        input("Enter the number of times the simulation should run: "))

    while number_of_simulations <= 50:
        number_of_simulations = int(
            input(
                "Enter the number of times the simulation should run (50 <): "))

except ValueError:
    print("You are supposed to enter a number, as such this will", end=" ")
    print("be simulated 51 times")
    number_of_simulations = 51

for i in range(number_of_simulations):
    roll_value = randint(1, 6)

    # if the roll value is 1, we increase on 0
    # if the roll value is 5, we increase on 4
    # basically roll_value_index = roll_value - 1

    roll_value_index = roll_value - 1

    simulation_result[roll_value_index] += 1

print(f"Simulation results for {number_of_simulations} rolls")

for i in range(6):
    print(f"{i + 1}: {simulation_result[i]}")
