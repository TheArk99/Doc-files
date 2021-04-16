from tkinter import *
import random, string
 #NOT WORKING MODULE
# import pyperclip

root = Tk()
root.geometry("400x400")
# root.resizable(0,0)

root.title("PASSWORD GENERATOR")

Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='Test', font ='arial 15 bold').pack(side = BOTTOM)

eLabel = Label(root, text = 'Enter Email\Site', font = 'arial 10 bold').pack()
email = Entry(root)
email.pack()

pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()

length = Spinbox(root, from_ = 1, to_ = 100, textvariable = pass_len , width = 15).pack()

pass_str = StringVar()
def Generator():
    password = ''

    for x in range(pass_len.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
   
    pass_str.set(password)

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()


passwords = str(pass_str)

filetext = open("Passwords.txt", "a")
filetext.write("\n     " + email.get() + ":") 
filetext.write("\n     " + passwords + "\n")
filetext.close()

    #NOT WORKING MODULE
# def Copy_password():
#     pyperclip.copy(pass_str.get())

# Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

root.mainloop()