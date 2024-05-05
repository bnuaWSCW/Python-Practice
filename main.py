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
else:
    print("Sadly, this is incorrect. The answer is 2")

# Next Question

print("Here is an even harder question:")
answerone = input("What is 12 x 12? ")

# Check The User's Answer and Give Feedback

if answerone == "144":
    print("Nice, you got it correct")
else:
    print("Inccorect, 12 x 12 is equal to 144")


# Question 3

print("Here is an even harder question about like terms:")
answertwo = input("Simplify: 2x+2k-4k: ")

# Check The User's Answer and Give Feedback

if answertwo == "2x-2k":
    print("Nice, that is correct.")
else:
    print("Nice try, but incorect. The answer is 2x-2k. Remember to add like terms together.")

#End The Quiz

print("Thank you for playing my quiz")
print("Have a great day",name)