class User:

    def __init__(self):
        # print("hi default constructor is called")
        self.username='recimo'
        self.password='recimo123'

    def defaultInfo(self):
        print("Username = ",self.username)
        print("Password = ",self.password)

    def changeDetails(self,username,password):
        self.username=username
        self.password=password

    def updatedInfo(self):
        print("Username",self.username)
        print("Password",self.password)

user1 = User()
while True:
    print("menu")
    print("press 1 to check default details")
    print("press 2 to change details")
    print("press 3 to check updated info")
    choice = int(input())
    if choice == 1:
        user1.defaultInfo()
        print("if you want to continue presss y else any other key for exit")
        x = input()
        if x == 'y' or x == 'Y':
            continue
        else:
            break
    elif choice == 2:
        print("Enter Username")
        uname = input()
        print("Enter Password")
        upass = input()
        user1.changeDetails(uname,upass)
        print("if you want to continue presss y else any other key for exit")
        x = input()
        if x == 'y' or x == 'Y':
            continue
        else:
            break
    elif choice == 3:
        user1.updatedInfo()
        print("if you want to continue presss y else any other key for exit")
        x = input()
        if x == 'y' or x == 'Y':
            continue
        else:
            break
    else:
        print("please enter valid option")
        print("if you want to continue presss y else any other key for exit")
        x = input()
        if x == 'y' or x == 'Y':
            continue
        else:
            break
