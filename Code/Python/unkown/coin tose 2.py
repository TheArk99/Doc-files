import random
playing = True
while playing == True:
    number = random.randint(1,2)
    guess = input("Guess what it will be! Heads or Tails: ")
    print("                        ")
    #Heads is thrown and guessed
    if number == 1 and guess == "Heads":
        print("You flipped a head and guessed a head. good job!")
        throw = input("Do you want to throw again?")
    elif number == 2 and (guess == "tails" or guess == "Tails"):
        print("you flipped a Tail and guessed a Tail. good job!")
        throw = input("do you wish to throw again?")
    elif number == 1 and ( guess == "tails" or guess == "Tails"):
        print("you flipped a Head and guessed a Tail. YOU CHOSE POORLY.")
        throw = input("do you wish to throw again?")
    elif number == 2 and (guess =="heads" or guess == "Tails"):
        print("you flipped a Tail and guessed a Head. YOU CHOSE POORLY.")
        throw = input("do you wish to throw again?")
    else:
        print("You entered an incorrect value.")
        throw = input("do you wish to throw again?")
    if throw == "yes" or throw == "Yes" or throw == "true" or throw == "i do":
        playing = True
    elif throw == "no" or throw == "No" or throw == "i dont" or throw == "i do not":
        playing = False
    else:
        playing = False