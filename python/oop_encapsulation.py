class Warrior:
    def __init__(self, name):
        self.name = name
        self._age = 0

    # getter function
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age should be greater than zero")


warrior1 = Warrior('worr_1')
print(warrior1.age)
warrior1.age = -5
print(warrior1.age)
