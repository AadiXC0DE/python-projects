import random

def trivia_quiz():
    print("Welcome to Trivia Quiz!")
    print("Answer the following trivia questions.")

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["Mars", "Venus", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],
            "answer": "Leonardo da Vinci"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "answer": "Blue Whale"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["O2", "CO2", "H2O", "N2"],
            "answer": "H2O"
        }
    ]

    score = 0

    for idx, question in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

        try:
            player_answer = int(input("Enter the number of your answer (1-4): "))
            if player_answer < 1 or player_answer > 4:
                raise ValueError("Invalid input. Please enter a number between 1 and 4.")

            selected_option = question['options'][player_answer - 1]
            if selected_option == question['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {question['answer']}")
        except ValueError as e:
            print(e)

    print("\nQuiz Finished!")
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    trivia_quiz()
