class SuperWarrior:
    def walk(self):
        print('Can walk without need for rest')


class NormalWarrior:
    def walk(self):
        print('Need a rest time while walking')


def check_walking_style(obj):
    obj.walk()


sup_warrior = SuperWarrior()
nor_warrior = NormalWarrior()

check_walking_style(sup_warrior)
check_walking_style(nor_warrior)
