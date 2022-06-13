import random


while True:
    try:
        your_choice = input("Enter a choice (R for Rock, P for Paper, S for Scissors): ")

        options = ["R", "P", "S"]
        CPU = random.choice(options)

        print( "player ({}), CPU ({})".format(your_choice,CPU))
        if your_choice == CPU:
            print(f"You both selected {your_choice}. It's a tie, No winner no Losser!")
        elif your_choice == "R":
            if CPU == "S":
                print("You win!")
                break
            else:
                print("CPU wins.")
                break
        elif your_choice == "P":
            if CPU == "R":
                print("You win!")
                break
            else:
                print("CPU wins.")
                break
        elif your_choice == "S":
            if CPU == "P":
                print("You win!")
                break
            else:
                print("CPU wins.")
                break
        else:
            print("invalid input")
    except:
        print("something is wrong")

