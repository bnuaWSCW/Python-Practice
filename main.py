# score

score = 0

# Ask The User Their Name And Store It

name = input("What is Your Name?")

# Greet The User And Introduce The Quiz

print("Hello, welcome to the quiz,", name)
print("This quiz is about maths")

# Ask The User A Question

answer = input("What is 1 + 1? ")

# Check The User's Answer and Give Feedback
if answer == "2":
    print("Nice, you got it correct")
    score +=1
elif answer == "":
    print("Please type in an answer")
    answer = input("What is 1 + 1?")
    if answer == "2":
        print("Nice, you got it correct")
        score +=1
    else: 
        print("Sadly, this is incorrect. The answer is 2")
else:
    print("Sadly, this is incorrect. The answer is 2")

# Next Question

print("Here is an even harder question:")
answerone = input("What is 12 x 12? ")

# Check The User's Answer and Give Feedback

if answerone == "144":
    print("Nice, you got it correct")
    score +=1
elif answerone == "":
    print("Please type in an answer")
    answerone = input("What is 12 x 12?")
    if answerone == "144":
        score +=1
        print("Nice, you got it correct. 12 x 12 is equal to 144")
    else:
        print("Incorroect, 12x12 is equal to 144")
else:
    print("Incorrect, 12 x 12 is equal to 144")


# Question 3

print("Here is an even harder question about like terms:")
answertwo = input("Simplify: 2x+2k-4k: ")

# Check The User's Answer and Give Feedback

if answertwo == "2x-2k":
    print("Nice, that is correct.")
    score +=1
elif answertwo == "":
    print("Please type in an answer")
    answertwo = input("Simplify: 2x + 2k - 4k:")
    if answertwo == "2x-2k":
        print("Nice, you got it correct")
        score +=1
    else:
        print("Nice try, but incorect. The answer is 2x-2k. Remember to add like terms together.")
else:
    print("Nice try, but incorect. The answer is 2x-2k. Remember to add like terms together.")

#End The Quiz

print("Thank you for playing my quiz")
print("Your final score is", score)
print("Have a great day",name)