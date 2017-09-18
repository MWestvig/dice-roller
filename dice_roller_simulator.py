import random


def roll_dice():
    num = random.randint(1, 6)
    print(num)


print("Here we go! Time to roll the dice.\n")
rolling = True

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
