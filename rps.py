#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#
import random
ROCK = "1"
SCISSOR = "2"
PAPER = "3"

print("Welcome to Rock, Paper, Scissors!")
print("Enter your hand")
print("1 - rock")
print("3 - paper")
print("2 - scissors")
player_choice = input()

computer_choice = str(random.randint(1,3))

if player_choice == computer_choice:
    print("tie")
elif (
    (player_choice == ROCK and computer_choice == SCISSOR)
    or (player_choice == SCISSOR and computer_choice == PAPER)
    or(player_choice == PAPER and computer_choice == ROCK)
    ):
    print("computer choice = "+computer_choice)
    print("You win")
else:
    print("computer choice = "+computer_choice)
    print("You lose")