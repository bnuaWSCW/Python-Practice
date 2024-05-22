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
        except Exception as e:
            print("That is not an integer", e)

    # Ask The User A Question

    question_tries = attempt
    for i in range(len(QUIZ_QUESTIONS)):
        while question_tries > 0:

            answer = input("{}\nA.{}\nB.{}\nC.{}\nD.{}\n".format(QUIZ_QUESTIONS[i], QUIZ_OPTIONS[i][0],
                                                QUIZ_OPTIONS[i][1],QUIZ_OPTIONS[i][2],QUIZ_OPTIONS[i][3])).lower()

            # Check The User's Answer and Give Feedback
            if answer == QUIZ_OPTIONS[i][QUIZ_ANSWERS[i]] or answer == QUIZ_LIST_OPTION[QUIZ_ANSWERS[i]].lower():
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



    if question_tries == 0:
        print("You have used up all of your attempts.")
    print("Your final score is {}".format(score))
    play = input("Would you like to play again?").lower()

#End The Quiz

print("Thank you for playing my quiz")
print("Have a great day {}".format(name))