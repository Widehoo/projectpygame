class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if target.hp > 0:
            if dis(target, actor) > self.range:
                print('Враг слишком далеко для оружия {}'.format(self.name))
            else:
                print('Врагу нанесен урон оружием {} в размере {}'.format(self.name, self.damage))
                target.hp -= self.damage
        else:
            print('Враг уже повержен')

    def __str__(self):
        return self.name


def dis(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


class BaseCharacter:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return self.x, self.y


class BaseEnemy(BaseCharacter):
    def __init__(self, x, y, weapon, hp):
        super().__init__(x, y, hp)
        self.weapon = weapon

    def hit(self, target):
        if type(target) == MainHero:
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return 'Враг на позиции ({}, {}) с оружием {}'.format(self.x, self.y, self.weapon)


class MainHero(BaseCharacter):
    def __init__(self, x, y, name, hp):
        super().__init__(x, y, hp)
        self.name = name
        self.weapon = None
        self.sp = []

    def hit(self, target):
        if len(self.sp):
            if type(target) == BaseEnemy:
                self.weapon.hit(self, target)
            else:
                print('Могу ударить только Врага')
        else:
            print('Я безоружен')

    def add_weapon(self, weapon):
        if type(weapon) == Weapon:
            print('Подобрал {}'.format(weapon))
            self.sp.append(weapon)
            if len(self.sp) == 1:
                self.weapon = weapon
        else:
            print('Это не оружие')

    def next_weapon(self):
        if len(self.sp) == 0:
            print('Я безоружен')
        elif len(self.sp) == 1:
            print('У меня только одно оружие')
        else:
            if self.weapon == self.sp[-1]:
                self.weapon = self.sp[0]
                print('Сменил оружие на {}'.format(self.weapon))
            else:
                self.weapon = self.sp[self.sp.index(self.weapon) + 1]
                print('Сменил оружие на {}'.format(self.weapon))

    def heal(self, amount):
        if self.hp + amount >= 200:
            self.hp = 200
            print('Полечился, теперь здоровья {}'.format(self.hp))
        else:
            self.hp += amount
            print('Полечился, теперь здоровья {}'.format(self.hp))