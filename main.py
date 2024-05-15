import random

GOOD_COMMENT = ["Nice job", "You're smart", "Cool", "Sigma"]

BAD_COMMENT = ["Dumb", "Keep on going", "Cmon", "Lock in"]

QUIZ_QUESTIONS = ["What is 1 + 1? ",
                  "What is 12 x 12? ",
                  "Simplify 2x+2k-4k:"]

QUIZ_OPTIONS = [["1" , "2" , "3" , "4"],
                ["144","1212","24","120"],
                ["-2k-2x", "2a+15", "2x-2k", "2x+2k"]]

QUIZ_LIST_OPTION = ["A","B","C","D"]

QUIZ_ANSWERS = [1,0,2]

QUESTION_FORMAT = {"{}\nA.{}\nB.{}\nC.{}\nD.{}\n"}

    # Ask The User Their Name And Store It

name = input("What is Your Name?")

# play
play = "yes"

while play == "yes".lower():

    # score

    score = 0

    # Greet The User And Introduce The Quiz

    print("Hello, welcome to the quiz,", name)
    print("This quiz is about maths")

    # Asks The User How Many Attempts They Want
    while True:
        try:
            attempt = int(input("How many attempts would you like for the quiz? 1, 2, 3 or 4 attempts?"))
            break
        except:
            print("That is not an integer")

    # Ask The User A Question

    question_tries = attempt

    while question_tries > 0:

        answer = input("{}\nA.{}\nB.{}\nC.{}\nD.{}\n".format(QUIZ_QUESTIONS[0], QUIZ_OPTIONS[0][0],
                                              QUIZ_OPTIONS[0][1],QUIZ_OPTIONS[0][2],QUIZ_OPTIONS[0][3])).lower()

        # Check The User's Answer and Give Feedback
        if answer == QUIZ_OPTIONS[0][QUIZ_ANSWERS[0]] or answer == QUIZ_LIST_OPTION[QUIZ_ANSWERS[0]]:
            print("Nice, you got it correct")
            print(random.choice(GOOD_COMMENT))
            score += 1
            break
        elif answer == "":
            print("Please type in an answer")
            answer = input("What is 1 + 1?")
            if answer == "2".lower():
                print("Nice, you got it correct")
                print(random.choice(GOOD_COMMENT))
                score += 1
            else:
                print("Sadly, this is incorrect.")
                print(random.choice(BAD_COMMENT))
                question_tries -= 1
                print("You have {} attempt(s) left".format(question_tries))
        elif answer in QUIZ_LIST_OPTION or answer in QUIZ_OPTIONS[0]:
            print("Sadly, this is incorrect.")
            print(random.choice(BAD_COMMENT))
            question_tries -= 1
            print("You have {} attempt(s) left".format(question_tries))

        else: 
            print("That wasn't an option")
            print(random.choice(BAD_COMMENT))
            question_tries -= 1
            print("You have {} attempt(s) left".format(question_tries))
            

    # Next Question
    while question_tries > 0:
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
            print(random.choice(GOOD_COMMENT))
            score += 1
            break
        elif answerone == "":
            print("Please type in an answer")
            answerone = input("What is 12 x 12?")
            if answerone == "144".lower():
                score += 1
                print("Nice, you got it correct. 12 x 12 is equal to 144")
                print(random.choice(GOOD_COMMENT))
            else:
                print("Incorrect")
                print(random.choice(BAD_COMMENT))
                question_tries -= 1
                print("You have {} attempt(s) left".format(question_tries))
        elif answerone != "a".lower() and answerone != "b".lower() and answerone != "c".lower() and answerone != "d".lower() and answerone != "144" and answerone != "1212" and answerone != "24" and answerone != "120":
            print("That wasn't an option")
            question_tries -= 1
            print("You have {} attempt(s) left".format(question_tries))
        else:
            print("Incorrect.")
            print(random.choice(BAD_COMMENT))
            question_tries -= 1
            print("You have {} attempt(s) left".format(question_tries))

    # Question 3
    while question_tries > 0:
        print("Here is an even harder question about like terms:")
        questiontwo = ("Simplify: 2x+2k-4k: ").lower()
        a2 = "-2k-2x"
        b2 = "2a+15"
        c2 = "2x-2k"
        d2 = "2x+2k"

        answertwo = input("{}\nA.{} \nB.{} \nC.{} \nD.{}\nAnswer:".format(questiontwo, a2, b2, c2, d2)).lower()

        # Check The User's Answer and Give Feedback
        if answertwo == c2.lower() or answertwo == "c".lower():
            print("Nice, that is correct.")
            print(random.choice(GOOD_COMMENT))
            score += 1
            break
        elif answertwo == "":
            print("Please type in an answer")
            answertwo = input("Simplify: 2x + 2k - 4k:")
            if answertwo == "2x-2k":
                print("Nice, you got it correct")
                print(random.choice(GOOD_COMMENT))
                score += 1
            else:
                print(
                    "Nice try, but incorect. Remember to add like terms together."
                )
                print(random.choice(BAD_COMMENT))
                question_tries -= 1
                print("You have {} attempt(s) left".format(question_tries))
        elif answertwo != "a".lower() and answertwo != "b".lower() and answertwo != "c".lower() and answertwo != "d".lower() and answertwo != "-2k-2x" and answertwo != "2a+15" and answertwo != "2x-2k" and answertwo != "2x+2k" or answertwo == "3":
            print("That wasn't an option")
        else:
            print(
                "Nice try, but incorect. Remember to add like terms together."
            )
            print(random.choice(BAD_COMMENT))
            question_tries -= 1
            print("You have {} attempt(s) left".format(question_tries))
    if question_tries == 0:
        print("You have used up all of your attempts.")
    print("Your final score is {}".format(score))
    play = input("Would you like to play again?").lower()

#End The Quiz

print("Thank you for playing my quiz")
print("Have a great day {}".format(name))
