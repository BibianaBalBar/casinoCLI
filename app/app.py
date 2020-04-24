from os import system, name
from time import sleep
from pyfiglet import figlet_format

from account import Account

def clear ():
    system('cls' if name =='nt' else 'clear')


acc = Account()
games = ['Card Game', 'Cho-han', 'Roulette', 'Blackjack', 'Slots']

system('cls' if name =='nt' else 'clear')
ascii = figlet_format('           Casino')
print(ascii)
print("For the game list type 'games'\nFor more commands type'help'\n")


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
        pass
    if user_input.lower() == 'exit':
        break

    #Games
    if user_input.lower() == 'dice' or user_input.lower() == 'chohan' or user_input.lower() == 'cho-han':
        pass

    if user_input.lower() == 'card' or user_input.lower() == 'card games':
        pass

    if user_input.lower() == 'blackjack':
        pass

    if user_input.lower() == 'slot' or user_input.lower() == 'slots':
        pass

    #Account and loans options
    if user_input.lower() == 'account' or user_input.lower() == 'balance':
        print(f'The current balance is: {money}')