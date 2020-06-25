import deck
import chips
import hand


def new_deck():
    global dealer_deck

    dealer_deck = deck.Deck()
    dealer_deck.shuffle()

    if len(dealer_deck) == 0:
        new_deck()

def hit():
    pass

def new_player(name, chips):
    return chips.Chips(name, chips)

while True:
    print("Welcome to Black Jack!")
    player_name = input('Please enter your name:')
    while True:
        try:
            player_chips = int(input('Enter the number of chips you have: '))
            break
        except ValueError:
            continue

    player = new_player()