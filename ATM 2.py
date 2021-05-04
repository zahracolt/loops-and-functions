import random

database = {}


def init():
    print('******* WELCOME ******')
    account = int(input('Do you have an account with us 1 (Yes) 2(N0)\n'))
    if account == 1:
        login()
    elif account == 2:
        register()
    else:
        print("Invalid option, please try again")
        init()


def register():
    print("******* Register ******")
    first_name = input('Enter your first name\n')
    last_name = input('Enter your last name\n')
    email = input("Enter your email address\n")
    password = input('enter your password\n')
    amount = 0

    account_number = account_generator()

    database[account_number] = [first_name, last_name, email, password, amount]
    print(f' {database}')

    print('You have successfully registered\n')
    print(f'Your account number is {account_number}')
    print('Keep it safe')
    print('=' * 30)

    login()


def login():
    print("******* LOGIN *******")
    email_from_user = input('Enter your email address\n')
    password = input('Enter your password\n')

    for accountNumber, UserDetails in database.items():
        if UserDetails[2] == email_from_user:
            if UserDetails[3] == password:
                menu()
        else:
            print('Invalid account or password')
            login()


def account_generator():
    return random.randrange(1111111111, 9999999999)


def menu():
    print(f"Welcome ")
    select_option = int(input("Select 1 (Deposit) 2 (Withdraw) 3 (Check Balance)\n"))
    if select_option == 1:
        deposit()
    elif select_option == 2:
        withdrawal()
    elif select_option == 3:
        check_balance()
    else:
        print("Invalid option, please try again")
        menu()


def withdrawal():
    print("******** WITHDRAW ******")
    for account_number, bal in database.items():
        print(f'Your current balance is {bal[4]}')
        print('=' * 30)
        withdraw_amount = int(input('Enter the amount to withdraw\n'))
        if withdraw_amount < bal[4]:
            bal[4] -= withdraw_amount
            print(f'Your new balance is {bal[4]}')
            another_tran()
        else:
            print('Insufficient Balance in your account\n')
            print('Enter a small amount')
            withdrawal()


def deposit():
    print("******* DEPOSIT ******")
    deposit_amount = int(input("Enter the amount to deposit\n"))
    print(f'You deposited {deposit_amount}')
    for account_number, bal in database.items():
        bal[4] += deposit_amount
        print(f'Your new balance is {bal[4]}')
        another_tran()


def another_tran():
    another_transaction = int(input('Do you need another transaction 1 (YES) 2 (NO)\n'))
    if another_transaction == 1:
        menu()
    elif another_transaction == 2:
        end_tran()

    else:
        print('Invalid option, please try again')
        another_tran()


def check_balance():
    print('******** CHECK BALANCE *******')
    for account_number, bal in database.items():
        print(f'Your account balance is {bal[4]}')
        another_tran()


def end_tran():
    pick = int(input("Are you sure you want to end the transaction 1 (Yes) 2 (NO)\n"))
    if pick == 1:
        print("Thank you for transacting with us")
        quit()
    elif pick == 2:
        another_tran()
    else:
        print("Invalid Option, please try again")
        end_tran()


init() 