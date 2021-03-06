class Deck:
    import random
    import card

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 11}

    def __init__(self):
        self.deck = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.deck.append(Deck.card.Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += f"\n {card.__str__()}"
        return "The Deck has: " + deck_comp

    def shuffle(self):
        Deck.random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
