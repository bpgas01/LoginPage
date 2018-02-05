# @ author Duncan Sykes
# version 0.0.4
# 12/2017

from tkinter import *
import os



bullet = "\u2022"  # specifies bullet character ad stores as a variable


def Meme_1():
    print('meme')


def adele():
    print(e1)


def run_skynet():
    os.system('python start.py')


def endProgram():  # this confirms if you definitly want to quit the program
    Button(root, text='Quit', fg='red', command=quit).grid(row=4)


def Login():
    try:
        with open('Storage.csv', 'rb') as data:
            print(data)
            print('Login info file loaded')
    except:
        with open('Storage.csv', 'wb') as data:
            print(data)
            print("Login Info file created")


def Sign_up():
    # the following code is used to create the GUI for the sign up form
    def Setup_details():
        def StoreData():

            # this code checks to see if the entered passwords are the same
            pass1 = s4.get()
            pass2 = s5.get()
            if pass1 == pass2:
                Button(root, text='Continue', command=adele, fg='green').grid(row=17, column=2)
            else:
                Warning = Tk()
                Warning.title('ERROR')
                Label(Warning, text="Passwords do not match, please try again").pack()
                Button(root, text='Continue', command=adele, fg='red').grid(row=17, column=2)
                Warning.mainloop()
                pass

        def showPass():
            s4 = Entry(root)
            s5 = Entry(root)

            s4.grid(row=15, column=1)
            s5.grid(row=15, column=1)

        # this is the start of the GUI load up
        ast1 = Label(root, text='*', fg='red')
        ast2 = Label(root, text='*', fg='red')
        ast3 = Label(root, text='*', fg='red')
        ast4 = Label(root, text='**', fg='red')
        ast5 = Label(root, text='**', fg='red')
        Label(root, text='Please fill out the required fields(*)').grid(column=1, row=10)

        Label(root, text='First name: ').grid(row=11)
        Label(root, text='Last name: ').grid(row=12)

        # ------------------------------------------

        Label(root, text='Username: ').grid(row=14)
        Label(root, text='Password: ').grid(row=15)
        Label(root, text='Confirm Password: ').grid(row=16)

        s1 = Entry(root)
        s2 = Entry(root)
        s3 = Entry(root)
        s4 = Entry(root, show=bullet)
        s5 = Entry(root, show=bullet)

        s1.grid(row=11, column=1)
        s2.grid(row=12, column=1)
        s3.grid(row=14, column=1)
        s4.grid(row=15, column=1)
        s5.grid(row=16, column=1)
        # ------------------------
        ast1.grid(row=11, column=2)
        ast2.grid(row=12, column=2)
        ast3.grid(row=14, column=2)
        ast4.grid(row=15, column=2)
        ast5.grid(row=16, column=2)

        Button(root, text='Restart Entries', command=Setup_details).grid(row=9)
        Button(root, text='Continue', command=StoreData).grid(row=17, column=2)
        Button(root, text='Show Password', command=showPass, fg='blue').grid(row=9, column=2)

    def CheckPin():
        # in ordeer for a person to sign up, they must first be provided with a 4 digit code
        # if it does not match the one in the system, the program will not allow the person to sign up
        pincheck = e3.get()
        if pincheck == '5086':
            Setup_details()

        else:
            master = Tk()
            Label(master, text='YOU ARE NOT AUTHORISED TO SIGN UP!', fg='red', font='30').pack()

    Label(root, text='Please Provide your 4 digit pin to sign up').grid(row=5, column=1)
    e3 = Entry(root)
    e3.grid(row=6, column=1)
    Button(root, text="Check", command=CheckPin).grid(row=7, column=1)


# The start of the program
# The variable 'root' is set to store the data to create and update a GUI widget or window
root = Tk()
root.title('*SIGN IN*')
# the Label code creates text within the window
# The grid element is a geomentric element that organises the GUI
Label(root, text="Please login:").grid()
Label(root, text='USERNAME: ').grid(row=2)
Label(root, text='PASSWORD: ').grid(row=3)
Button(root, text='Debug', fg='blue', command=Meme_1).grid(row=0, column=3)
# In order to have multiple functional entry boxes, multiple varibles must be usd to carry and store data
# This is done to prevent logical errors
e1 = Entry(root)
e2 = Entry(root, show=bullet)  # instead of showing the letters in the password, it shows the standard bullet points

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)

# The Button code places usable buttons in the GUI which can perform different commands
# commands used by buttons can even be used to call subprograms
Button(root, text='Quit', command=endProgram).grid(row=4)
Button(root, text="Continue", command=Login).grid(column=1, row=4)
Button(root, text="Sign Up", command=Sign_up, fg='green').grid(column=2, row=4)
Button(root, text='RUN', command=run_skynet, fg='blue').grid(column=3, row=4)  # for debuging and dev purposes only...
root.mainloop()  # creates an end point for the GUI to loop from without it, the GUI won't load