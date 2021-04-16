name = input("type your name... ")
password = input("what is your password?... ")
if password == "0908" and name == "Noah" :
    question = int(input(name + " " + "do you want to do a math trick, a cube root calculator, a sci notation calc,or a coin toss?...Type 1. for math trick, 2. for calculator, type 3. for a coin tose, type 4. for sci notation calc,or type 0. to leave..."))
    if question != int(0):
        if question == int(2):
            cube = int(input(name + " " + "chose a number to calculate the cube root... "))
            epsilon = 0.01
            guess = 0.0
            increment = 0.00001
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
            print("what do you want to gues on?...")
            a = input("type here what you want to guess on first... ")
            b = input("type here what you want to guess on with it... ")
            import random
            playing = True
            while playing == True:
                number = random.randint(1,2)
                guess = input("Guess what it will land on! " + a + " or " + b + ": ")
                print("                        ")
                if number == 1 and (guess == a or guess == a):
                    print("You flipped the coin and got a " + a + " and guessed a " + a + ". good job!")
                    throw = input("Do you want to throw again?")
                elif number == 2 and (guess == b or guess == b):
                    print("you flipped the coin and got a " + b + " and guessed a " + b + ". good job!")
                    throw = input("Do you wish to throw again?")
                elif number == 1 and ( guess == b or guess == a):
                    print("you flipped the coin and got a " + a + " and guessed a " + b + ". YOU CHOSE POORLY.")
                    throw = input("Do you wish to throw again?")
                elif number == 2 and (guess == a or guess == b):
                    print("you flipped the coin and got a " + b + " and guessed a " + a + ". YOU CHOSE POORLY.")
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
        elif question == int(4):
            want = int(input("Do you want to have the sum of the two or the full number of one? type 1. for sum, 2. for full number... "))
            a = float(input("Type First Sicentific notation 1... "))
            ex = int(input("Type type the first expontent 1... "))
            
            def  sinotation(i): 
                    """
                    
                
            1        Parameters
                    ----------
                    i : finds the sum of scinentifc notations
                
                    Returns
                    -------
                    The xeponent.
                
                    """  
                    exponent = 10 ** i  
                    return exponent
            
            aplusex = a * sinotation(ex)
                
                
            if want == 1: 
                b = float(input("Type second Sicentific notation 1... "))
                er = int(input("Type type the second expontent 2... "))
                sign = input("Type what sign it has for the mdas... ")
                bpluser = b * sinotation(er)
                if sign == "*":
                    scinot1 = aplusex * bpluser
                    print(scinot1)
                elif sign == "/":
                    scinot2 = aplusex / bpluser
                    print(scinot2)
                elif sign == "+":
                    scinot3 = aplusex + bpluser
                    print(scinot3)
                elif sign == "+":
                    scinot4 = aplusex - bpluser
                    print(scinot4)
            elif want == 2:
                print(aplusex)                        
        else:
            print("                                             ")
            print("no do it again... wrong input... stop GOOFIN!")
    else:
        print("thank you for useing this program hope to see you again soon. ")
else:
    print("                                             ")
    print("to bad you are not me! ): GO AWAY! ")
        
        