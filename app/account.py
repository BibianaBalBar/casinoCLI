class Account:
    """Creates and mantains the accounts and loans
    """
    def __init__(self, money=100, loan=0, max_loan=1000):
        self.money = money
        self.loan = loan
        self.max_loan = max_loan

    def __repr__(self):
        return f'Wallet: {self.money} Loan: {self.loan}'

    def check_balance(self):
        return f'Current balance: {self.money}'

    def check_loan(self):
        return f'Current debt {self.loan}'
    
    def complete_acc(self):
        print(f'\nComplete extract\nWallet:{self.money}\nDebt:{self.loan}\n')

    def take_loan(self, amount):
        try:
            if amount < 0:
                print('Please use a positive number.')
            elif amount > self.max_loan:
                if self.max_loan == 0:
                    print('You cannot take any more debts for now.') 
                else:
                    print(f'You only have {self.max_loan} available to request.')
            else:
                self.max_loan -= amount
                self.loan += amount
                self.money += amount
        except TypeError:
            print(f'Please specify the amount.\n{amount} is not a recognized value')

    def pay_loan(self, amount):
        try:
            if amount < 0:
                print('Please use a positive number.')  
            elif self.loan == 0:
                print('You do not have any debt!')
            elif amount > self.loan:
                print(f"You're trying to pay more than you owe!\nCurrent debt:{self.loan}") 
            else:
                self.max_loan += amount
                self.loan -= amount
                self.money -= amount
        except TypeError:
            print(f'\nPlease specify the amount.\n{amount} is not a recognized value\n')


