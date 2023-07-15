import random


def generate_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def get_user_guess():
    while True:
        guess = input("Enter your guess (in the format R,G,B): ")
        try:
            red, green, blue = map(int, guess.split(","))
            if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
                return red, green, blue
            else:
                print("Invalid RGB values. Please try again.")
        except ValueError:
            print("Invalid input. Please enter three integers separated by commas.")


def calculate_score(color, guess):
    red_diff = abs(color[0] - guess[0])
    green_diff = abs(color[1] - guess[1])
    blue_diff = abs(color[2] - guess[2])
    return 100 - (red_diff + green_diff + blue_diff)


def main():
    print("Color Game")
    print("Guess the RGB values of the color!")

    color = generate_color()
    attempts = 0
    while True:
        guess = get_user_guess()
        attempts += 1
        score = calculate_score(color, guess)

        if score == 100:
            print("Congratulations! You guessed the color correctly!")
            print("Number of attempts:", attempts)
            break
        else:
            print("Incorrect guess. Your score:", score)

    print("Thank you for playing!")


if __name__ == '__main__':
    main()
