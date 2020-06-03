from random import randint, choice
from app.deck_cards import Card, Deck
from app.account import Account

# Cho-han game - chose Odd or Even 
def cho_han(bet, choice):
    bet = int(bet)
    n = randint(1,12)
    print(f'The number is {n}.')
    if choice.lower() == 'even':
        if n % 2 == 0:
            print('You won!')
            return bet
        else:
            print('You lose!')
            return -bet
    else:
        if n % 2 == 0:
            print('You lose!')
            return -bet
        else:
            print('You won!')
            return bet



# Card Game - higher card wins
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


#Slot with numbers - match 3 numbers
def slot(bet):
    bet = int(bet)
    n1 = randint(1,5)
    n2 = randint(1,5)
    n3 = randint(1,5)
    print(f'Your Slot numbers are: {n1} - {n2} - {n3}')
    if n1 == n2 == n3:
        print("You won!")
        return bet
    else:
        print("You lose!")
        return -bet


#Roulette
def roulette(bet, choice):
    bet = int(bet)
    n = randint(0, 36)
    print(f'The number is {n}.')
    if choice.lower() == 'even':
        if n % 2 == 0:
            print('You won!')
            return bet
        else:
            print('You lose!')
            return -bet
    elif choice.lower() == 'odd':
        if n % 2 == 0:
            print('You lose!')
            return -bet
        else:
            print('You won!')
            return bet
    elif choice == str(n):
        print('You won!')
        return bet
    else:
        print('You lose!')
        return -bet