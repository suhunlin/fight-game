from player_class import Player
from monster_class import Monster
class Game:
    def __init__(self,*args):
        self.players = []
        for name in args:
            self.players.append(Player(name=name))

g1 = Game('Allen', 'Chloe', 'Ryan')

def main():
    g1 = Game('Allen', 'Chloe', 'Ryan')
    m1 = Monster()
    g1.players[0].fight(g1.players[2])
    m1.practice_big_monster(g1.players[2])
    # m1.practice_mid_monster(g1.players[0])
    # m1.practice_small_monster(g1.players[0])

if __name__ == '__main__':
    main()




