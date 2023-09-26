
#   including libraries
from MUserDL import MUserDL
from MUserUI import MuserUI
import os
from time import sleep

#Defining main function

def main():
    path="Data.txt"
    MUserDL.readDataFromFile(path)
    option=0
    while(option!=3):
        os.system("cls")
        option=MuserUI.menu()
        if(option==1):
            user=MuserUI.takeInputWithoutRole()
            user=MUserDL.SignIn(user)
            if(user!=None):
                if(user.isAdmin()):
                    print("This is Admin")
      
                  #Admin Menu(complete programm)
                else:
                    print("This is User")
                    #User Menu(continue programm)
                sleep(3)
        elif(option==2):
            user=MuserUI.TakeInputFromConsole()
            MUserDL.addUserIntoList(user)
            MUserDL.storeUserIntoFile(user,path)

#Calling Main Function as the code starts executing
if __name__=="__main__":
    main()