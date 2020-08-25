import random

class Gambler:

    def start_gamble(self):
        stake = 100
        return stake


    def win(self, stake):
        stake += 1
        return stake


    def loose(self, stake):
        stake -= 1
        return stake


    def check_resign(self, initial_stake, stake):
        if stake <= initial_stake // 2 or stake >= initial_stake // 2:
            return True
        return False

gambler = Gambler()
initial_stake = gambler.start_gamble()