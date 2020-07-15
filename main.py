from time import sleep
from app.account import Account
from app.modu import clear, intro, helper
from app.games import pick_a_card, cho_han, slot, roulette, blackjack

acc = Account()
games = ['Card Game', 'Cho-han', 'Roulette', 'Blackjack', 'Slots']

intro()
while True:

    user_input = input('>> ')

#Settings and general options
    if user_input.lower() == 'games':
        print()
        for g in games:
            print(g)
            sleep(0.4)
        print()
    if user_input.lower() == 'clear':
        clear()
    if user_input.lower() == 'help':
        helper()
    if user_input.lower() == 'exit':
        break

#Games
    if user_input.lower() == 'dice' or user_input.lower() == 'chohan' or user_input.lower() == 'cho-han' or user_input.lower() == 'cho':
        bet = input(f'How much to bet>> ')
        choice = input(f'Do you bet on odd or even? ')
        game = cho_han(bet, choice)
        acc.money += int(game)

    if user_input.lower() == 'card' or user_input.lower() == 'card games':
        bet = input(f'How much to bet>> ')
        game = pick_a_card(bet)
        acc.money += int(game)

    if user_input.lower() == 'blackjack':
        pass

    if user_input.lower() == 'slot' or user_input.lower() == 'slots':
        bet = input(f'How much to bet>> ')
        game = slot(bet)
        acc.money += int(game)

    if user_input.lower() == 'roulette' or user_input.lower() == 'roulete':
        bet = input(f'How much to bet>> ')
        choice = input(f'Do you bet on odd or even or a number? ')
        game = roulette(bet, choice)
        acc.money += int(game)

    if user_input.lower() == 'blackjack' or user_input.lower() == 'black' or user_input.lower() == '21':
        bet = input(f'How much to bet>> ')
        game = blackjack(bet)
        acc.money += int(game)
    

#Account and loans options
    if user_input.lower() == 'account' or user_input.lower() == 'balance':
        acc.complete_acc()
    
    if user_input.lower() == 'take loan':
        amount = input(f'You can take a loan up to: {acc.max_loan}\nAmount?>> ')
        try:
            acc.take_loan(int(amount))
            print(acc.check_loan())
        except ValueError:
            print(f'Please specify the amount.\n{amount} is not a recognized value')
    
    if user_input.lower() == 'pay loan':
        amount = input(f'Your debt is: {acc.loan}\nAmount to pay?>> ')
        try:
            acc.pay_loan(int(amount))
            print(acc.check_loan())
        except ValueError:
            print(f'Please specify the amount.\n{amount} is not a recognized value')
        

# Test game to delete after 
    if user_input.lower() == 'test':
        while True:
            bet = input(f'How much to bet>> ')
            choice = input(f'even or odd?\n>> ')
            if choice == 'odd' or choice == 'even':
                game = cho_han(bet, choice)
                acc.money += int(game)
                cont = input('Continue?(y/n)\n>> ')
                if cont.lower() == 'n':
                    break
                
                