# play
play = "yes"

while play == "yes":

    # score

    score = 0

    # Ask The User Their Name And Store It

    name = input("What is Your Name?")

    # Greet The User And Introduce The Quiz

    print("Hello, welcome to the quiz,", name)
    print("This quiz is about maths")

    # Asks The User How Many Attempts They Want
    while True:
        try:
            attempt = int(input("How many attempts would you like per question? 1, 2, 3 or 4 attempts?"))
            break
        except:
            print("That is not an integer")

    # Ask The User A Question

    question_tries = attempt

    while question_tries > 0:
        question = ("What is 1 + 1? ")
        a = "1"
        b = "2"
        c = "3"
        d = "4"
        answer = input("{}\nA.{} \nB.{} \nC.{} \nD.{}\nAnswer:".format(question, a, b, c, d)).lower()

        # Check The User's Answer and Give Feedback
        if answer == "2" or answer == b or answer == "b":
            print("Nice, you got it correct")
            score += 1
            break
        elif answer == "":
            print("Please type in an answer")
            answer = input("What is 1 + 1?")
            if answer == "2".lower():
                print("Nice, you got it correct")
                score += 1
            else:
                print("Sadly, this is incorrect. The answer is 2, or B")
        elif answer != "a".lower() and answer != "b".lower() and answer != "c".lower() and answer != "d".lower() and answer != "4" and answer != "3" and answer != "2" and answer != "1":
            print("That wasn't an option")
        else:
            print("Sadly, this is incorrect.")
            question_tries -= 1
        if question_tries == 0:
            ("You have no attempts left.")

    # Next Question

    print("Here is an even harder question:")
    questionone = ("What is 12 x 12? ").lower()
    a1 = "144"
    b1 = "1212"
    c1 = "24"
    d1 = "120"

    answerone = input("{}\nA.{} \nB.{} \nC.{} \nD.{}\nAnswer:".format(questionone, a1, b1, c1, d1)).lower()

    # Check The User's Answer and Give Feedback

    if answerone == "144".lower() or answerone == "A".lower() or answerone == "a":
        print("Nice, you got it correct")
        score += 1
    elif answerone == "":
        print("Please type in an answer")
        answerone = input("What is 12 x 12?")
        if answerone == "144".lower():
            score += 1
            print("Nice, you got it correct. 12 x 12 is equal to 144")
        else:
            print("Incorroect, 12x12 is equal to 144")
    elif answerone == "I don't know" and answerone == "IDK".lower() and answerone == "?":
        print("Not sure?")
        print("The answer is 144")
    elif answerone != "a".lower() and answerone != "b".lower() and answerone != "c".lower() and answerone != "d".lower() and answerone != "144" and answerone != "1212" and answerone != "24" and answerone != "120":
        print("That wasn't an option")
    else:
        print("Incorrect, 12 x 12 is equal to 144")

    # Question 3

    print("Here is an even harder question about like terms:")
    questiontwo = ("Simplify: 2x+2k-4k: ").lower()
    a2 = "-2k-2x"
    b2 = "2a+15"
    c2 = "2x-2k"
    d2 = "2x+2k"

    answertwo = input("{}\nA.{} \nB.{} \nC.{} \nD.{}\nAnswer:".format(questiontwo, a2, b2, c2, d2)).lower()

    # Check The User's Answer and Give Feedback

    if answertwo == c.lower() or answertwo == "c".lower():
        print("Nice, that is correct.")
        score += 1
    elif answertwo == "":
        print("Please type in an answer")
        answertwo = input("Simplify: 2x + 2k - 4k:")
        if answertwo == "2x-2k":
            print("Nice, you got it correct")
            score += 1
        else:
            print(
                "Nice try, but incorect. The answer is 2x-2k. Remember to add like terms together."
            )
    else:
        print(
            "Nice try, but incorect. The answer is 2x-2k. Remember to add like terms together."
        )
    
    play = input("Would you like to play again?")

#End The Quiz

print("Thank you for playing my quiz")
print("Your final score is {}".format(score))
print("Have a great day {}".format(name))
