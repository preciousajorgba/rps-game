import random

your_choice = input("Enter a choice (R for Rock, P for Paper, S for Scissors): ")

options = ["R", "P", "S"]
CPU = random.choice(options)

print( "player - {} , CPU - {}".format(your_choice,CPU))

if your_choice == CPU:
    print(f"You both selected {your_choice}. It's a tie, No winner no Losser!")
elif your_choice == "R":
    if CPU == "S":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! You lose.")
elif your_choice == "P":
    if CPU == "R":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! You lose.")
elif your_choice == "S":
    if CPU == "P":
        print("Scissors beats paper! You win!")
    else:
        print("Rock beats scissors! You lose.")
