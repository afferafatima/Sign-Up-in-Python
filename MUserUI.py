from MUser import MUser

class MuserUI:

    @staticmethod
    def menu():
        print("1. SignIn")
        print("2. SignIUp")
        print("Enter Option")
        option=int(input())
        return option

    @staticmethod
    def printList(usersList):
        for user in usersList:
            print(user.userName,user.userPassword,user.userRole)

    @staticmethod
    def TakeInputFromConsole():
        userName=input("Enter UserName")
        userPassword=input("Enter UserPassword")
        userRole=input("Enter UserRole")
        user=MUser(userName,userPassword,userRole)
        return user
    @staticmethod
    def takeInputWithoutRole():
        userName=input("Enter UserName")
        userPassword=input("Enter UserPassword")
        user=MUser(userName,userPassword,None)
        return user