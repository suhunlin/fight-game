from player_class import Player
class Monster:
    def __init__(self):
        self.exp = 0
        self.count = 0
        self.init_small_monster()
        self.init_mid_monster()
        self.init_big_monster()

    def init_big_monster(self):
        self.hp_big = 20
        self.attack_big = 15
        print('產生大怪物:hp:', self.hp_big, '攻擊力：', self.attack_big)

    def init_mid_monster(self):
        self.hp_mid = 10
        self.attack_mid = 10
        print('產生中怪物:hp:', self.hp_mid, '攻擊力：', self.attack_mid)

    def init_small_monster(self):
        self.hp_small = 5
        self.attack_small = 5
        print('產生小怪物:hp:', self.hp_small, '攻擊力：', self.attack_small)

    def practice_big_monster(self,target):
        if isinstance(target,Player):
            while self.hp_big != 0:
                self.count += 1
                self.hp_big -= target.attack
                target.hp -= self.attack_big
                if target.hp <= 0:
                    print('戰鬥了',self.count,'次，打大怪獸失敗!!!你已經死了!!!')
                    break
            if self.hp_big == 0:
                target.attack_change(attack_modify=3)
                print('攻擊次數：',self.count)
                print(target.name, 'attack大怪獸',self.count,'次,經過訓練增加', str(3), 'hp剩餘：', target.hp)
            self.init_big_monster()
            self.count = 0

    def practice_mid_monster(self,target):
        if isinstance(target,Player):
            while self.hp_mid != 0:
                self.count += 1
                self.hp_mid -= target.attack
                target.hp -= self.attack_mid
                if target.hp <= 0:
                    print('戰鬥了',self.count,'次，打中怪獸失敗!!!你已經死了!!!')
                    break
            if self.hp_mid == 0:
                target.attack_change(attack_modify=2)
                print(target.name, 'attack中怪獸',self.count,'次,經過訓練增加', str(2), 'hp剩餘：', target.hp)
            self.init_mid_monster()
            self.count = 0

    def practice_small_monster(self,target):
        if isinstance(target,Player):
            while self.hp_small != 0:
                self.count += 1
                self.hp_small -= target.attack
                target.hp -= self.attack_small
                if target.hp <= 0:
                    print('戰鬥了',self.count,'次，打小怪獸失敗!!!你已經死了!!!')
                    break
            if self.hp_small == 0:
                target.attack_change(attack_modify=1)
                print(target.name, 'attack小怪獸',self.count,'次,經過訓練增加', str(1), 'hp剩餘：', target.hp)
            self.init_small_monster()
            self.count = 0







