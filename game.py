import json, random

FILE_NAME = 'questions.json'


# Retrieves the questions from JSON file
try:
    with open(FILE_NAME, "r") as file:
        questions = json.load(file)
except FileNotFoundError:
    print("Internal Error: Record file not found")
    exit()

print("WELCOME TO QUIZ GAME")



# Handles invalid input
try: 
    question_no = int(input(f"How many questions do you want? Enter number less than {len(questions)}: "))
    while (question_no >= len(questions) ) or question_no < 1:
        print("Invalid input, try again")
        question_no = int(input(f"\nEnter number less than {len(questions)}: "))

        # exit()

except ValueError:
    print("\nInvalid Input. Enter valid number")
    exit()


correct = 0
wrong = 0
numbers = []

# Generates random number that isn't equal to each other
while len(numbers) < question_no:
    random_no = random.randint(0, len(questions)-1)

    if (random_no not in numbers) and (len(numbers) != question_no):
        numbers.append(random_no)




for numb in numbers:
    # Represent one question object from the json file
    question_line = questions[numb]

    
    question = question_line["question"]
    options = question_line["options"]
    answer = question_line["answer"]

    print("\n" + question)

    user_answer = input(f"Enter options {options}. Enter answer: ")

    if answer == user_answer:
        correct += 1
        print("Correct")

    else:
        wrong += 1
        print("Wrong")

print(f"\nResult: Total score is {correct}. You got {wrong} {"question" if wrong < 2 else "questions"} wrong")



