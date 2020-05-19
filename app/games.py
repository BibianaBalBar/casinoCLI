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
def pick_a_card(bet):
    bet = int(bet)
    deck = Deck()
    deck.shuffle()
    player_card = deck.deal_card()
    print(f"You're card is {player_card}")    
    comp_card = deck.deal_card()
    print(f"Computer's card is {comp_card}")      
    pcard = str(player_card)[:2]
    def pc(pcard):
        if pcard not in ['02', '03', '04', '05', '06', '07', '08', '09', '10']:    
            if pcard == ' J':
                return '11'
            elif pcard == ' Q':
                return '12'
            elif pcard == ' K':
                return '13'
            elif pcard == ' A':
                return '14'            
        return pcard
    ccard = str(comp_card)[:2]
    def cc(ccard):
        if ccard not in ['02', '03', '04', '05', '06', '07', '08', '09', '10']:
            if ccard == ' J':
                return '11'
            elif ccard == ' Q':
                return '12'
            elif ccard == ' K':
                return '13'
            elif ccard == ' A':
                return '14'            
        return ccard
    if int(pc(pcard)) > int(cc(ccard)):
        print("You won!")
        return bet
    else:
        print("You lose!")
        return -bet

pick_a_card(100)