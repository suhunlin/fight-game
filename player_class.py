class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 5
        self.__protect_money = 1000

    def hp_change(self, hp_modify):
        self.hp = hp_modify

    def attack_change(self, attack_modify):
        self.attack += attack_modify

    def fight(self, target):
        if isinstance(target,Player):
            self.hp -= target.attack
            print(self.name,'被',target.name,'攻擊扣hp',target.attack,'剩餘hp:',self.hp)

    def practice(self,attack_modify):
        print(self.name,'通過修行,attack增加',attack_modify)
        self.attack_change(attack_modify)

    @property
    def money(self):
        return self.__protect_money

    @money.setter
    def money(self, money_change):
        self.__protect_money = money_change



