import random

def main():
    flashcards = [
        {
            "question": "What is a Positional Argument?",
            "answer": "An argument that can be called by their position in the function definition."
        },
        {
            "question": "What is a Keyword Argument?",
            "answer": "An argument that can be called by their name in the function call."
        },
        {
            "question": "What is a Default Argument?",
            "answer": "An argument that is given a default value in the function definition."
        },
        {
            "question": "Explain how to use a Default Argument with an example.",
            "answer": "Using the function signature 'def calculate_taxi_price(miles_to_travel, rate, discount=10):', "
                      "the discount has a default value of 10. It can be overridden by providing a different value when calling the function."
        },
        {
            "question": "What happens if you call 'calculate_taxi_price(100, 10)'?",
            "answer": "The function uses the default value for discount (10) and calculates the price based on 100 miles at a rate of 10 per mile."
        }
    ]

    while True:
        flashcard = random.choice(flashcards)
        print("Flashcard Question: ")
        print(flashcard["question"])
        input("Press Enter to reveal the answer...")
        print("Answer: ")
        print(flashcard["answer"])
        if input("Press Enter to continue or type 'exit' to quit: ").lower() == 'exit':
            break

if __name__ == "__main__":
    main()
