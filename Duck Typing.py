class Dog:
    def sound(self):
        print("bark bark")


class Cat:
    def sound(self):
        print("Meow Meow")


def Make_Sound(animal):
    animal.sound()



Make_Sound(Dog())
Make_Sound(Cat())
