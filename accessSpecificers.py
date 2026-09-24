class Student:
    _name = "Karan"

s = Student()
print(s._name)     # technically ✅



class Parent:
    def __init__(self):
        self.__data = 10


class Child(Parent):
    def show(self):
        print(self._Parent__data)   # ❌

c = Child()
c.show()
