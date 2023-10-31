import os #operating system
import subprocess

def read_balance(txtfile):
        if os.path.exists(txtfile):
            with open(txtfile, 'r') as f:
                  balance = float(f.read())
            return balance
        else: 
            balance = 0
            with open(txtfile, 'w') as f:
                f.write(str(balance))
            return balance
        
def withdraw_amount(amount, txtfile):
    if os.path.exists(txtfile):
        with open(txtfile, 'r') as f:
            balance = float(f.read())
        new_balance = balance - amount
        with open(txtfile, 'w') as f:
            f.write(str(new_balance))
        return new_balance
        
    else:
        with open(txtfile, 'w') as f:
            f.write(str(-amount))
        return -amount
        
def deposit_amount(amount, txtfile):
    if os.path.exists(txtfile):
        with open(txtfile, 'r') as f:
            balance = float(f.read())
            new_balance = balance + amount
        
        with open(txtfile, 'w') as f:
            f.write(str(new_balance))
            return new_balance
           
    else:
        with open(txtfile, 'w') as f:
            f.write(str(amount))
            return amount
        
def checkbook():
    txtfile = 'balance.txt'
   
    while True:
        print('~~~ Welcome to your terminal checkbook! ~~~')
        print('Input a number from 1 to 4 to initiate: ') 
        print('1. View Balance' )
        print('2. Withdraw amount' )
        print('3. Deposit amount') 
        print('4. exit: ')

        customer_question = input('What would you like to do? ')

        if customer_question == '1':
            balance = read_balance(txtfile)
            print(f'Your balance is: $ {balance:.2f} \n')
            
        elif customer_question == '2':
            amount = float(input('Enter the withrawal amount: $ '))
            new_balance = withdraw_amount(amount, txtfile)
            print(f'You withdrew the amount of: $ {amount} \n')  
            print(f'Your new current balance is: $ {new_balance} \n')

        elif customer_question == '3':
            amount = float(input('Enter the deposit amount: $ '))
            new_balance = deposit_amount(amount, txtfile)
            print(f'You deposited the amount of: $ {amount} \n')
            print(f'Your new current balance is: $ {new_balance} \n')
            
           
        elif customer_question == '4':
            print('Thank you for using Terminal Checkbook \n')
            break

        else:
            print('You have entered a wrong input, please try again! \n')
        

checkbook()
