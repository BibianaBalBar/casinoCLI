from random import randint, choice
from deck_cards import Card, Deck

# Test game to delete after 
def test(bet, choice):
    bet = int(bet)
    n = randint(1,12)
    if choice == 'even':
        if n % 2 == 0:
            print('win')
            return bet
        else:
            print('lose')
            return -bet
    else:
        if n % 2 == 0:
            print('lose')
            return -bet
        else:
            print('won')
            return bet



# Card Game
