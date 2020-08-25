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


gambler = Gambler()
initial_stake = gambler.start_gamble()
