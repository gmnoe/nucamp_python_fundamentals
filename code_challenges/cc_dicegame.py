import random

high_score = 0


def dice_game():
    global high_score
    while True:
        print("Current High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        response = input("Enter your choice: ")
        if response == "1" or response.casefold() == "roll dice":
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            print("\nYou roll a... ", dice_1)
            print("You roll a... ", dice_2, "\n")
            total = dice_1 + dice_2
            print("You have rolled a total of: ", total, "\n")
            if total > high_score:
                high_score = total
                print("New High Score!\n")
        elif response == "2" or response.casefold() == "leave game":
            print("Goodbye!")
            break




dice_game()