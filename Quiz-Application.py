print("=====QUIZ-APPLICATION=====")

questions = [
    {
        "questions": "What is the output of print(2 + 3)?",
        "options": ["1", "5", "23", "Error"],
        "answer": "5"
    },
    {
        "questions": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "questions": "Which data type is used to store multiple values in Python?",
        "options": ["int", "float", "list", "string"],
        "answer": "list"
    },
    {
        "questions": "What is the correct file extension for Python files?",
        "options": [".pt", ".pyt", ".py", ".python"],
        "answer": ".py"
    },
    {
        "questions": "Which loop is used to iterate over a sequence in Python?",
        "options": ["while", "loop", "for", "repeat"],
        "answer": "for"
    }
]


while(1):
    print("Menu")
    print("1.Start Quiz")
    print("2.Exit")

    choice = int(input("Enter your choice : "))

    if(choice==1):
        score = 0
        for q in questions:
            print("Question:")
            print(q["questions"])
            print("options:")
            for i in range(len(q["options"])):
                print(i+1,".",q["options"][i])

            user_answer = int(input("Enter option number : "))

            if(user_answer<1 or user_answer>len(q["options"])):
               print("Invalid option number")
               print("Enter the valid option number")

            selected_answer = q["options"][user_answer-1]
            print("You selected :",selected_answer)

            if(selected_answer==q["answer"]):
                print("Correct answer")
                score += 1

            else:
                print("Wrong answer")
                print("Correct answer is",q["answer"])

    elif(choice==2):
        print("\nExiting Quiz Application.")
        print("Thankyou for participating!")
        break

    else:
        print("Invalid choice. Enter the choice again")

        
