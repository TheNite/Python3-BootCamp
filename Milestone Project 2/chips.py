class Chips:

    def __init__(self, player_name, total=200):
        self.player_name = player_name
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lost_bet(self):
        self.total -= self.bet
