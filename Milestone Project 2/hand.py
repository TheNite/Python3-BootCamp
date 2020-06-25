class Hand:
    import deck

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += Hand.deck.Deck.values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def current_cards(self):
        cards = []
        for card in self.cards:
            cards.append(card.__str__())

        return cards

    def __str__(self):
        return f'Current Cards: {self.current_cards()}\nTotal Value: {self.value}'