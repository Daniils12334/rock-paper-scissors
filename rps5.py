#
# ROCK, PAPER, SCISSORS - Iterācija 2
# 
# 4. Pārkopēt šeit iepriekšējo failu, modificēt spēli no iepriekšēja faila, lai ir pieci raundi un beigas rādas cik sanāca vinnēt (izmantot for loop, https://www.w3schools.com/python/python_for_loops.asp)
# 5. [Bonus Level] Izmantot ne vairāk par trīs if/else rezultāta skaitīšanai (var izmantot ciparu starpību)
# 6. [UNSTOPPABLE] Pievieno papildus ieročus Rock-Paper-Scissors-Spock-Lizard (https://en.wikipedia.org/wiki/Rock_paper_scissors#Additional_weapons)
# 
import random
ROCK = "1"
SCISSOR = "2"
PAPER = "3"
SPOCK = "4"
LIZARD = "5"
x = 0
y = 0
z = 0

for _ in range(5):
    print("Welcome to Rock, Paper, Scissors! 5 Rounds version")
    print("Enter your hand")
    print("1 - rock")
    print("3 - paper")
    print("2 - scissors")
    print("4 - spock")
    print("5 - lizard")
    player_choice = input()
    computer_choice = str(random.randint(1,3))
    if player_choice == computer_choice:
        print("tie")
        z = z+1
    elif (
        (player_choice == ROCK and computer_choice == SCISSOR) or (player_choice == ROCK and computer_choice == LIZARD)
        or (player_choice == SCISSOR and computer_choice == PAPER)or (player_choice == SCISSOR and computer_choice == LIZARD)
        or(player_choice == PAPER and computer_choice == ROCK) or (player_choice == PAPER and computer_choice == SPOCK)
        or(player_choice == SPOCK and computer_choice == SCISSOR) or (player_choice == SPOCK and computer_choice == ROCK)
        or(player_choice == LIZARD and computer_choice == SPOCK)or(player_choice == LIZARD and computer_choice == PAPER)
        ):
        print("computer choice = "+computer_choice)
        print("You win")
        x = x+1
    else:
        print("computer choice = "+computer_choice)
        print("You lose")
        y=y+1
        print("Next round")
print("your wins")
print(x)
print("your loses")
print(y)
print("your ties")
print(z)


