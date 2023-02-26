class Warrior:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    @abstractmethod
    def walk(self):
        pass
