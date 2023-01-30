#Imports
import time
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
class Window(QMainWindow):
   def __init__(self):
       super().__init__()
 
       self.setGeometry(300, 300, 600, 400)
       self.setWindowTitle("PyQt5 window")
       self.show()
 
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
#Functions
def username(firstname,surname,year,form):
    user = surname + firstname[0] + year[2:4] + form[len(form)-1]
    return user

def showmenu():
    print("\t         Menu")
    print("╔════════════════════════════╗")
    print("   1: Create an Account")
    print("   2: Read Account Info")
    print("   3: Delete an Account")
    print("   4: Sign In Simulation")
    print("   5: Show Menu")
    print("   6: Exit Program")
    print("╚═════════════════════════════╝\n")

#Menu
while True:
    showmenu()
    choice = input("Make a selection:\n> ")
    time.sleep(1)

    if choice == "1":
    #Creating the Account
        surname = input("What is your surname?:  ")
        firstname = input("What is your first name:  ")
        year = input("When did you join?:  ")
        form = input("What is your form?:   ")
        password = input("Please enter a password:  ")
        userFile = open(username(surname,firstname,year,form)+".txt","w")
        userFile.write(firstname+" "+surname+"\n"+year+"\n"+form+"\n"+username(surname,firstname,year,form)+"\n")
        userFile.write(password) 
        userFile.close()
        print("Thank you for using this!\nYour username is " +(username(firstname,surname,year,form)))
        newEntry = input("Type x to quit, anything else to continue:    ")
        if newEntry == "x":
            print("Thank you for using this this service!\nWe hope to see you again :)")
            time.sleep(15)
            sys.exit()

    if choice == "2":
        username = input("Please enter your username:   ")
        userFile = open(username+".txt", "r") 
        content = userFile.read() 
        print(content) 
        userFile.close() 
        input()

    if choice == "3":
        n=5
        username = input("Please enter the username of the account you would like to delete:  ")
        userFile = open(username+".txt", "r")
        passcontent = userFile.readline(n)
        print(passcontent)
        passcheck = input("Please enter the password of said account:  ")
       # if passcontent == passcheck:
        #    os.path.exists(username+".txt")
         #   os.remove(userFile)
       # else:
        #    print("The account does not exist or password is incorrect")

        line = userFile.readline

        while line:
            if line == passcheck:
                os.path.exists(username+".txt")
                os.remove(userFile)

    input()   







    #loop menu

    if choice == "5":
        print("You are already in the menu!\n")

    #End code

    if choice == "6":
        print("Thank you for using this this service!\nWe hope to see you again :)")
        time.sleep(15)
        sys.exit()

    #End of the End.

    if int(choice) >= 6 or int(choice) <= 0:
        print("Invalid Answer, Please enter a correct value.\n")


