# - Lists - #
TOP_TEN = ["France", "Spain", "United States", "Italy", "Turkey", "Mexico", "United Kingdom", "Germany","Greece","Austria"]

#------ FUNCTIONS ------#

#- Introduces the quiz -#


def intro():

  name = input("What is your name?")

  print("Welcome to this quiz, {}".format(name))
  print("This quiz is about guessing the top 10 most visited countries in the world")

def getLives():

  while True:
    try:
      attempts = input("How many chances would you like?")
      attempts = int(attempts)
      if attempts > 0:
        return attempts
      else:
        print("Please type in a positive number")
    except:
      print("That is not a number")

def inList(question,TOP_TEN):
  if question in TOP_TEN:
    return True
  else:
    return False
#------ MAIN CODE ------#

score = 0 

intro()
lives = getLives()

while lives > 0:
  question = input("\nName the top 10 most visited countried in the world:\n").lower()

  if inList(question, TOP_TEN) == True:
    score =+ 5
    print("Nice, you're correct")
  else:
    lives -= 1
    print("That is incorrect.\nYou have {} lives left".format(lives))

print("You're out of lives. Game Over")