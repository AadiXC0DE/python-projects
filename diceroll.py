import random

def roll_dice():
    print("Dice Roll Generator")
    while True:
        print("\nMenu:")
        print("1. Roll the dice")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            input("Press Enter to roll the dice...")
            dice_roll = random.randint(1, 6)
            print(f"The dice rolled: {dice_roll}")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")


roll_dice()
