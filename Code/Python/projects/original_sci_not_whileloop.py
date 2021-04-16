#sicentific notation
while True:
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