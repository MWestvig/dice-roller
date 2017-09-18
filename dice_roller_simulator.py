import random


# The function to roll the die, it chooses a random number between 1 and 6 and prints it.
def roll_dice():
    num = random.randint(1, 6)
    print("Rolling...")
    print(num)


print("Here we go! Time to roll the dice.\n")
rolling = True

# Rolls the die and then asks the user whether they want to roll again, and exits if they do not, or if they enter an unknown answer.
while rolling:
    roll_dice()
    ans = input("\nRoll Again? (Yes or No): ")
    if ans == "Yes":
        rolling = True
    elif ans == "No":
        rolling = False
    else:
        print("Unknown answer, ending.")
        rolling = False

print("\nThanks for rolling, bye!")
