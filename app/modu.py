from os import system, name
from pyfiglet import figlet_format

def clear ():
    system('cls' if name =='nt' else 'clear')

def intro():
    system('cls' if name =='nt' else 'clear')
    ascii = figlet_format('           Casino')
    print(ascii)
    print("For the game list type 'games'\nFor more commands type'help'\n")


def helper():
    system('cls' if name == 'nt' else 'clear')
    print(figlet_format('Help:'))
    print ("""
    For the games list type 'games';

    To check wallet type 'balance';

    To take a loan type 'take loan';

    To pay the loan 'pay loan';

    To clear the screan type 'clear';

    To quit type 'exit'
    
    """)