class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        return f"{self.name} | Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack}"

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, other):
        if not self.is_alive():
            print(f"{self.name} не може атакувати — мертвий.")
            return
        if not other.is_alive():
            print(f"{other.name} вже мертвий.")
            return
        other.health -= self.attack
        print(f"{self.name} атакує {other.name} на {self.attack} шкоди.")
        if other.health <= 0:
            other.health = 0
            print(f"{other.name} переможений!")

class Warrior(Character):
    def __init__(self, name, level):
        super().__init__(name, level, health=150 + level * 10, attack=20 + level * 2)
        self.armor = 30

    def heal(self):
        self.health += 20
        print(f"{self.name} (Warrior) відновлює 20 здоров'я.")

class Mage(Character):
    def __init__(self, name, level):
        super().__init__(name, level, health=100 + level * 5, attack=30 + level * 3)
        self.mana = 100

    def heal(self):
        self.health += 15
        self.mana -= 10
        print(f"{self.name} (Mage) використовує магію для відновлення 15 здоров'я.")

class Archer(Character):
    def __init__(self, name, level):
        super().__init__(name, level, health=120 + level * 7, attack=25 + level * 2)
        self.arrows = 10

    def heal(self):
        self.health += 10
        print(f"{self.name} (Archer) перев'язує рани та відновлює 10 здоров'я.")

if __name__ == "__main__":
    warrior = Warrior("Рома", level=3)
    mage = Mage("Артем", level=2)
    archer = Archer("Поліна", level=4)

    print(warrior.info())
    print(mage.info())
    print(archer.info())

    print("\n--- Початок бою ---")

    warrior.attack_enemy(mage)
    mage.attack_enemy(warrior)
    archer.attack_enemy(warrior)

    print("\n--- Відновлення ---")
    warrior.heal()
    mage.heal()
    archer.heal()

    print("\n--- Стан після бою ---")
    print(warrior.info())
    print(mage.info())
    print(archer.info())
