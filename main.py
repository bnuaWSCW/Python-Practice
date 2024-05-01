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
if answer != "2":
    print("Sadly, that is incorrect. The answer is 2")

# Next Question

print("Here is an even harder question:")
input("What is 12 x 12? ")

# Tells The Correct Answer To Question 2

print("The answer is 144")

# Question 3

print("Here is an even harder question about like terms:")
input("Simplify: 2xc+2k+2x+3c+14cx-14k: ")

# Answer To Question 3

print("The answer is: 16cx+2x+2c-12k")

#End The Quiz

print("Thank you for playing my quiz")
print("Have a great day",name)