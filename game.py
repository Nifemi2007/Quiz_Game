import json, random

FILE_NAME = 'questions.json'



# functions
def user_input():
    try: 
        question_no = int(input(f"How many questions do you want? Enter number less than {len(questions)}: "))
        while (question_no >= len(questions) ) or question_no < 1:
            print("Invalid input, try again")
            question_no = int(input(f"\nEnter number less than {len(questions)}: "))

            # exit()
   
    except ValueError as e:
        question_no = str(e)

    return question_no




def singular_check(inp):
    if inp < 2:
        return "question"
    else:
        return "questions"

# Retrieves the questions from JSON file
try:
    with open(FILE_NAME, "r") as file:
        questions = json.load(file)
except FileNotFoundError:
    print("Internal Error: Record file not found")
    exit()




choice = "y"
while choice == "y":
    print("\nWELCOME TO QUIZ GAME")

    
    # Handles invalid input
   
    question_no = user_input()
    while (type(question_no) != int):
        print("\nInvalid Input. Enter valid number")
        question_no = user_input()


    correct = 0
    wrong = 0
   

    random.shuffle(questions)
    questions_to_ask = questions[0:question_no]


  

# validate the user answer

    for quest in questions_to_ask:

        
        question = quest["question"]
        options = quest["options"]
        answer = quest["answer"]
        answer_index = 0
        available_options = []

        print("\n" + question)
        
        
        # Print options
        start = 97
        for i,opt in enumerate(options):
            print(chr(start + i),"->", opt)

            available_options.append(chr(start + i))
            if opt == answer:
                answer_index = i

        


        user_answer = input(f"Enter answer: ").lower()

        # Reject user_input that is not in available options
        while (user_answer not in available_options) and (user_answer not in options):
            print("Option not available\n")
            user_answer = input(f"Enter answer: ").lower()
        

        # to accept either alphabet or type the answer
        if (user_answer == answer )or (user_answer == chr(start + answer_index)):
            correct += 1
            print("Correct")

        else:
            wrong += 1
            print("Wrong")


    average = round(correct/question_no, 2) * 100
    print(f"\nResult is {average}%. You got {correct} {singular_check(correct)} correct and {wrong} {singular_check(wrong)} wrong ")
    # print(f"\nResult: Total score is {correct}. You got {wrong} {"question" if wrong < 2 else "questions"} wrong")

    choice = input("\nDo you want to try again? Enter y/n: ").lower()
    if choice == "n":
        print("\nThank you for playing!!!")

