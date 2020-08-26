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
        if stake <= initial_stake // 2 or stake >= initial_stake + (initial_stake // 2):
            return True
        return False


    def print_money(self, day, win_money, loss_money):
        if day > 20:
            print("Win Money on", day, "day is", win_money)
            print("Money Lost on", day, "day is", loss_money)
            print()


    def stake_difference(self, previous_stake, current_stake):
        return current_stake - previous_stake


    def find_lucky_unlucky(self, diction):
        win = []
        loss = []
        for key in diction:
            win.append(diction.get(key)[0])
            loss.append(diction.get(key)[1])
        for key in diction:
            if max(win) == diction.get(key)[0]:
                lucky = key
            if min(loss) == diction.get(key)[1]:
                unlucky = key
        return lucky, unlucky

def play():
    gambler = Gambler()
    next_month_check = initial_stake = gambler.start_gamble()
    stake = initial_stake
    days = 0
    win_money = 0
    loss_money = 0
    luck_determine = {}
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
        if gambler.stake_difference(initial_stake, stake) > 0:
            print("Won Money on day",days,"is", gambler.stake_difference(initial_stake, stake))
        else:
            print("Lost Money on day",days ,"is", -1 * gambler.stake_difference(initial_stake, stake))
        luck_determine[days] = [win_money, loss_money]
        lucky_day, unlucky_day = gambler.find_lucky_unlucky(luck_determine)
        initial_stake = stake + 100
        gambler.print_money(days, win_money, loss_money)
        win_money = 0
        loss_money = 0
        if next_month_check > stake and days == 30:
            continue
    print("Lucky Day", lucky_day)
    print("Unlucky Day",unlucky_day)
play()
