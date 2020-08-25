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


    def print_money(self, day, win_money, loss_money):
        if day > 20:
            print("Win Money on", day, "day is", win_money)
            print("Money Lost on", day, "day is", loss_money)
            print()

gambler = Gambler()
initial_stake = gambler.start_gamble()
stake = initial_stake
days = 0
win_money = 0
loss_money = 0
while days <= 29:
    days += 1
    while True:
        bet = random.random()
        if bet >= 0.5:
            stake = gambler.win(stake)
            win_money += 1
        else:
            stake = gambler.loose(stake)
            loss_money += 1
        if gambler.check_resign(initial_stake, stake):
            break
    gambler.print_money(days, win_money, loss_money)
    win_money = 0
    loss_money = 0
#     print("Stake on", days," day", initial_stake)
# print(days)