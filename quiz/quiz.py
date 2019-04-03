def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option

def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("OK then, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    f = open("questions.txt", "a")
    f.write(question + "\n")
    f.write(answer + "\n")
    f.close()

def ask_questions():
    questions = []
    answers = []
    
    # At the end of the with block the file is automatically closed
    with open("questions.txt", "r") as f:
        lines = f.read().splitlines()
    
    # This is going to turn each of these lists into a tuple with
    # a line number stored in i and the text stored in 'text'
    # if the line number is even then it is a question, if it
    # is odd, then it is an answer.
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)

    num_of_qs = len(questions)
    qs_and_as = zip(questions, answers)
    
    score = 0
    
    # The zip function puts these tuples together
    for question, answer in qs_and_as:
        guess = input(question + "> ")
        if guess.lower() == answer.lower():
            score += 1
            print("Correct!")
            print("Your current score: {0}".format(score))
        else:
            print("Sorry, that is incorrect")
            
    print("You got {0} correct out of {1}".format(score, num_of_qs))

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option")

        print("")
        
game_loop()

