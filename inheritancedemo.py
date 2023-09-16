class Vehicle:
    def __init__(self):
        print("parent constructor")

    def speed(self):
        print("20 km/hr")

    def tyre2(self):
        print("2 wheeler")

    def tyre4(self):
        print("4 wheeler")


class MarutiSuzuki(Vehicle):

    def color(self):
        # super()
        super().tyre4()
        print("red color")


# class Hyundai(Vehicle,MarutiSuzuki):
#     def ev(self):
#         print("ev car")


mobj = MarutiSuzuki()
mobj.color()
# mobj.tyre2()


# obj = Hyundai()
