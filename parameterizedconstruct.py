# class User:
#     def __init__(self,uname,upass):
#         self.username = uname
#         self.password = upass
#
#     def displayDetails(self):
#         print("Username ",self.username)
#         print("Password",self.password)
#
#
# print("Enter Username")
# uname = input()
# print("Enter Password")
# upass = input()
# u1 = User(uname,upass)
# u1.displayDetails()

class Demo:

    def test1(self):
        print("this is instance method")

    @classmethod
    def test2(cls):
        print("hii how are you this is class method")

    @staticmethod
    def test3():
        print("hello there this is static method")

Demo().test1()
Demo.test2()
Demo.test3()