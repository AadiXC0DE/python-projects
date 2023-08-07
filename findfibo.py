# Find out, Fibonacci!" is an engaging Python game that invites users to explore the fascinating world of the Fibonacci sequence. This interactive program offers two exciting options:

# Check a Number: Users can input a number, and the program will swiftly determine whether it belongs to the illustrious Fibonacci sequence. A clear verdict is provided, offering insights into the numerical wonders of this sequence.

# Explore the Sequence: For those curious about the Fibonacci sequence itself, the game allows users to specify the number of terms they wish to unveil. With each term's revelation, the mesmerizing sequence unfolds, showcasing the intrinsic beauty of Fibonacci's mathematical creation.
def is_perfect_square(n):
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

def is_fibonacci_number(number):
    if number < 0:
        return False

    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)

def display_instructions():
    print("Welcome to Find out, Fibonacci!")
    print("This game checks whether a given number belongs to the Fibonacci sequence.")
    print("You can also explore a portion of the Fibonacci sequence.")
    print("Enter 'q' to quit the game.\n")

def main():
    display_instructions()

    while True:
        choice = input("Do you want to check a number (1) or explore a portion (2) of the Fibonacci sequence? ")

        if choice == '1':
            number = int(input("Enter a number to check if it belongs to the Fibonacci sequence: "))
            if is_fibonacci_number(number):
                print(f"{number} is a Fibonacci number.\n")
            else:
                print(f"{number} is not a Fibonacci number.\n")

        elif choice == '2':
            n_terms = int(input("Enter the number of terms you want to explore: "))
            a, b = 0, 1
            count = 0

            print("Fibonacci sequence:")
            while count < n_terms:
                print(a, end=' ')
                a, b = b, a + b
                count += 1
            print("\n")

        elif choice.lower() == 'q':
            print("Thank you for playing Find out, Fibonacci!")
            break

        else:
            print("Invalid choice. Please enter '1', '2', or 'q'.\n")

if __name__ == "__main__":
    main()
