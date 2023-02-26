class Warrior:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self._is_mobile = True

    def walk(self):
        while self._is_mobile:
            print('walking')

    def lose_stick(self):
        self._is_mobile = False


class SuperWarrior(Warrior):
    def __init__(self, age, name):
        super().__init__(age, name)
        self._binaculars = True


class NormalWarrior(Warrior):
    pass
