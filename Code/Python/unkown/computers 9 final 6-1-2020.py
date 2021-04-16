name = input("type your name... ")
question = int(input(name + " " + "do you want to do a math trick, a cube root calculator, or a coin toss?...Type 1. for math trick, 2. for calculator, type 3. for a coin tose..."))
if question == int(2):
    cube = int(input(name + " " + "chose a number to calculate the cube root... "))
    epsilon = 0.01
    guess = 0.0
    increment = 0.000001
    num_guesses = 0
    while abs(guess**3 - cube) >= epsilon and guess <= cube:
        guess += increment
        num_guesses += 1
    print('num_guesses =', num_guesses)
    if abs(guess**3 - cube) >= epsilon:
        print('Failed on cube root of', cube)
    else:
        print(guess, 'is close to the cube root of', cube)
elif question == int(1): 
    mathQ = int(input(name + " " + "chose a number between 1-20... type your number... but i already think i know your number... i think it will be three... Now chose wisely... "))
    lines = ("          ") * 3
    print(lines * 5)
    print("add one...")
    print(lines)
    print("if you add one you should get this for your number..." + " ")
    add = (mathQ + int(1))
    print(add)
    print(lines)
    print("now double your number...") 
    double = add * int(2)
    print("now you should get this number...")
    print(double)
    print(lines)
    print("now add 4")
    print("you should get...")
    print("                 ")
    add4 = (double + int(4))
    print(add4)
    print(lines)
    print("now divid by 2... your should get...")
    divid = (add4 / int(2))
    print(divid)
    print(lines)
    print("now subtract the original number you chose...")
    print("now it should be...")
    print(lines)
    subtractorigin = (divid - mathQ)  
    print(subtractorigin)
elif question == int(3):
    import random
    playing = True
    while playing == True:
        number = random.randint(1,2)
        guess = input("Guess what it will land on! Heads or Tails: ")
        print("                        ")
        if number == 1 and (guess == "Heads" or guess == "heads"):
            print("You flipped the coin and got a head and guessed a head. good job!")
            throw = input("Do you want to throw again?")
        elif number == 2 and (guess == "tails" or guess == "Tails"):
            print("you flipped the coin and got a Tail and guessed a Tail. good job!")
            throw = input("Do you wish to throw again?")
        elif number == 1 and ( guess == "tails" or guess == "Tails"):
            print("you flipped the coin and got a Head and guessed a Tail. YOU CHOSE POORLY.")
            throw = input("Do you wish to throw again?")
        elif number == 2 and (guess =="heads" or guess == "Tails"):
            print("you flipped the coin and got a Tail and guessed a Head. YOU CHOSE POORLY.")
            throw = input("Do you wish to throw again?")
        else:
            print("You entered an incorrect value.")
            throw = input("Do you wish to throw again?")
        if throw == "yes" or throw == "Yes" or throw == "true" or throw == "i do":
            playing = True
        elif throw == "no" or throw == "No" or throw == "i dont" or throw == "i do not":
            playing = False
        else:
            playing = False
else:
    print("                                             ")
    print("no do it again... wrong input... stop GOOFIN!")
    