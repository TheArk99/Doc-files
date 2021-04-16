#sicentific notation
Q = int(input("Do you want to continue?...type 1. to continue, type 2. to quite loop... "))
while Q == 1:
    a = float(input("Type First Sicentific notation 1... "))
    ex = int(input("Type type the first expontent 1... "))
    b = float(input("Type second Sicentific notation 1... "))
    er = int(input("Type type the second expontent 2... "))
    
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
    elif sign == "-":
        scinot4 = aplusex - bpluser
        print(scinot4)
    
