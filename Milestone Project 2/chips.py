class Chips:

    def __init__(self, total=200):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lost_bet(self):
        self.total -= self.bet
