# - Lists - #
guesses = []
TOP_TEN = ["France", "Spain", "United States", "Italy", "Turkey", "Mexico", "United Kingdom", "Germany", "Greece", "Austria"]

#------ FUNCTIONS ------#

#- Introduces the quiz -#


def intro():

  name = input("Type In Your Username: ")

  print("Welcome to this quiz, {}".format(name))
  print("This quiz is about guessing the top 10 most visited countries in the world")

def getLives():

  while True:
      attempts = input("How many chances would you like?\n")
      try:
        attempts = int(attempts)
        if attempts > 0:
          return attempts
        else:
          print("Please type in a positive number")
      except:
        print("That is not a number")

def inList(answer, list):
  if answer in list:
    return True
  else:
    return False
  

#------ MAIN CODE ------#
play = "Yes".lower()

while play == "yes".lower():

  intro()
  lives = getLives()
  score = 0 

  while lives > 0 and score < 10:
    answer = input("\nName the top 10 most visited countried in the world:\n").title()

    inList(answer, TOP_TEN)

    if inList(answer, TOP_TEN) == True:
      if inList(answer, guesses):
        print("You have already guessed that")
      else:
        score += 1
        print("Nice, you're correct")
        guesses.append(answer)
        print("You have guessed {} country(s) with {} live(s) left. Right now, your score is {} out of 10".format(len(guesses), lives, score))
        if  int(len(guesses)) > 0:
          print("\nYou have guessed the following CORRECT countries:")
          print(guesses)
        elif int(len(guesses)) == 10:
          break
    else:
      lives -= 1
      print("That is incorrect.\nYou have {} lives left with a score of {}.".format(lives, score))
      if int(len(guesses)) > 0:
        print("You have guessed the following countries:")
        print(guesses)


  if lives == 0:
    print("You're out of lives.\nYour final score was {}\nGame Over.".format(score))
    play = input("\nWould you like to play again?").lower

  if score == 10 or int(len(guesses)) == 10:
    print("\nCongrats, you have guessed all ten of the most visted countries in the world")
    print("Thank you for playing")
    play != "Yes".lower()
    break
    

