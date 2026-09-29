import sqlite3
from datetime import datetime

# STEP 1 Database creating
# make a connection with database
connection = sqlite3.connect('atm.db')
cursor = connection.cursor()

# STEP 2
# Making first table into the database,  accounts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS 
accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_no TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    pin TEXT NOT NULL,
    account_type TEXT NOT NULL,
    balance REAL NOT NULL
)
""")

# STEP 3
# Making a table into the database for transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS 
transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_no TEXT NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    balance_after REAL NOT NULL,
    created_at TEXT NOT NULL
)
""")


# STEP 2 create some dummy accounts
# Account no 1
cursor.execute("""
INSERT OR IGNORE INTO accounts 
(account_no, name, pin,
account_type, balance)
VALUES (?, ?, ?, ?, ?)
""", ('100001', 'Abul', '1234', 'Savings', 100000))

# Account no 2
cursor.execute("""
INSERT OR IGNORE INTO accounts 
(account_no, name, pin, 
account_type, balance)
VALUES (?, ?, ?, ?, ?)
""", ('100002', 'Babul', '5678', 'Current', 200000))

# Account no 3
cursor.execute("""
INSERT OR IGNORE INTO accounts 
(account_no, name, pin,
account_type, balance)
VALUES (?, ?, ?, ?, ?)
""", ('100003', 'Karim', '4321', 'Savings', 300000))

# Account no 4
cursor.execute("""
INSERT OR IGNORE INTO accounts 
(account_no, name, pin, 
account_type, balance)
VALUES (?, ?, ?, ?, ?)
""", ('100004', 'Dulal', '8765', 'Current', 400000))

# Account no 5
cursor.execute("""
INSERT OR IGNORE INTO accounts 
(account_no, name, pin, 
account_type, balance)
VALUES (?, ?, ?, ?, ?)
""", ('100005', 'Ebadot', '1111', 'Savings', 500000))

# Account no 6
cursor.execute("""
INSERT OR IGNORE INTO accounts 
(account_no, name, pin, 
account_type, balance)
VALUES (?, ?, ?, ?, ?)
""", ('100006', 'Faijul', '2222', 'Current', 600000))


connection.commit()
connection.close()

# STEP 4 define function start here
#  create get_account()
def get_account(account_no):
    connection = sqlite3.connect('atm.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM accounts
    WHERE account_no = ?
    """, (account_no,))

    account = cursor.fetchone()

    connection.close()
    return account

# # function call will be outside from main function
# account = get_account('100001')
# print(account)

# STEP 5
# verify pin when user entered the pin
def verify_pin(account_no, entered_pin):
    # call get_account() for filter account_no
    account = get_account(account_no)
    if account is None:
        return False
    # stored the pin on the accounts table list no 3 there have the pin assest
    stored_pin = account[3]
    if entered_pin == stored_pin:
        return True
    else:
        return False

# result = verify_pin('100001', '1234')
# print(result)

# STEP 6
# Athenticate_user function
def athenticate_user(account_no, messages):
    # call get_account() for filter account_no
    account = get_account(account_no)
    if account is None:
        return None
    entered_pin = input(messages['enter_pin'])
    if verify_pin(account_no, entered_pin):
        return account
    else:
        print(messages['invalid_pin'])
        return None

# account = athenticate_user('100001')
# print(account)

# STEP 7
# show language menu function
def show_language_menu():
    print('1. Bangla')
    print('2. English')
    print('3. Malay')

def select_language():
    while True:
        choice = input('Select language: ')
        if choice == '1':
            return 'Bangla'
        elif choice == '2':
            return 'English'
        elif choice == '3':
            return 'Malay'
        else:
            print('Invalid choice. Please select 1, 2, or 3.')

# show_language_menu()
# language = select_language()
# print('Select language:', language)

def load_language(language):
    if language == 'Bangla':
        return {
            'welcome': 'ATM এ স্বাগতম,{name}!', 
            'enter_pin': 'PIN দিন',
            'invalid_pin': 'ভুল PIN',
            'balance': 'আপনার ব্যালেন্স',
            'account_not_found': 'একাউন্ট পাওয়া যায়নি',

            'withdraw': 'টাকা উত্তোলন ',
            'balance_inquiry':'ব্যালান্স দেখুন',
            'transfer': 'ট্রান্সফার',
            'exit': 'বের হয়ে যান',
            'atm_menu': 'এটিএম মেনু',

            'select_account_type': 'একাউন্টের  ধরণ নির্বাচন করুন',
            'savings': 'সেভিংস',
            'current': 'কারেন্ট',
            'invalid_account_type': 'একাউন্ট টাইপ ভুল',
            
        }
    elif language == 'English':
        return {
            'welcome': 'Welcome to ATM,{name}!',
            'enter_pin': 'Enter PIN',
            'invalid_pin': 'Invalid PIN',
            'balance': 'Your balance',
            'account_not_found': 'Account not found.',

            'withdraw': 'Withdraw ',
            'balance_inquiry':'Balance Inquiry',
            'transfer': 'Transfer',
            'exit': 'Exit',
            'atm_menu': 'ATM MENU',

            'select_account_type': 'Select Account Type',
            'savings': 'Savings',
            'current': 'Current',
            'invalid_account_type': 'Invalid Account Type',
        }
    elif language == 'Malay':
        return {
            'welcome': 'Salamat datang ke ATM,{name}!',
            'enter_pin': 'Masukkan PIN',
            'invalid_pin': 'PIN tidak sah',
            'balance': 'Baki anda',
            'account_not_found': 'Akaun tidak de jumpai',

            'withdraw': 'Pengeluaran',
            'balance_inquiry':'Semakan Baki',
            'transfer': 'Pemindahan',
            'exit': 'Keluar',
            'atm_menu': 'MENU ATM',

            'select_account_type': 'Pilih Jenis Akaun',
            'savings': 'Simpanan',
            'current': 'Semasa',
            'invalid_account_type': 'Jenis akaun Tidah Sah',
        }
    else:
        return None

# language = load_language('Malay')
# print(language['welcome'])
# print(language['enter_pin'])
# print(language['balance'])

# STEP 8.1 --show_main_menu()
def show_main_menu(messages):
    print(f'\n===== {messages['atm_menu']} =====')
    print(f'1.{messages['withdraw']}')
    print(f'2.{messages['balance_inquiry']}')
    print(f'3.{messages['transfer']}')
    print(f'4.{messages['exit']}')
    

# get menu choice by user
def get_menu_choice():
    while True:
        choice = input('Select an option: ')
        if choice in ['1', '2', '3', '4',]:
            return choice
        print('Invalid choice. Please select 1-4.')

# show_main_menu()
# choice = get_menu_choice()
# print('Your choice:', choice)

# STEP 15 Main Menu Loop Functionality
# Create atm_menu()
def atm_menu(account_no, messages):
    while True:
        show_main_menu(messages)
        choice = get_menu_choice()
        if choice == '1':
            account_type = select_account_type(messages)
            if not validate_account_type(account_no, account_type):
                print(messages['invalid_account_type'])
                continue
            amount = select_withdraw_amount()

            new_balance = withdraw_money(account_no, amount)
            if new_balance is None:        
                print('Withdraw failed.')
            else:
                save_transaction(account_no, 'withdraw', amount, new_balance)
                dispense_cash(amount)
                print(f"Withdraw successful.")
                print(f"Your remaining balance: {new_balance:.2f}")
                if ask_for_receipt():
                    transaction = { 
                        'account_no': account_no,
                        'transaction_type': 'Withdraw',
                        'amount': amount,
                        'balance_after': new_balance,
                        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    print_receipt(transaction)

        elif choice == '2':
            balance = get_balance(account_no)
            if balance is not None:
                show_balance(balance)
                
                if ask_for_receipt():
                    transaction = {
                        'account_no': account_no,
                        'transaction_type': 'Balance Inquiry',
                        'amount': 0,
                        'balance_after': balance,
                        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    print_receipt(transaction)
            else:
                print('Unable to get balance.')
            
        elif choice == '3':
            receiver_account_no = get_receiver_account()
            if verify_recevier(receiver_account_no):
                print('Receiver verified.')
    
                amount = get_transfer_amount()
                print(f"Transfer amount: {amount:.2f}")
    
                balance = get_balance(account_no)
                if validate_transfer(balance, amount):
                    result = transfer_money(
                        account_no,
                        receiver_account_no,
                        amount
                    )
                    if result:
                        print('Transfer successful.')
                        if ask_for_receipt():
                            transaction = {
                                'account_no': account_no,
                                'transaction_type': 'Transfer Sent',
                                'amount': amount,
                                'balance_after': get_balance(account_no),
                                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            }
                            print_receipt(transaction)
                    else:
                        print('Transfer failed.')
                else:
                    print('Insufficient balance.')
            else:
                print('Receiver account not found.')
        elif choice == '4':
            eject_card()
            break

# STEP 9 (Balance Inquiry) Start
# Step 9.1 get balance function
def get_balance(account_no):
    # get the data with fetch from database
    account = get_account(account_no)
    if account is None:
        return None
    balance = account[5]
    return balance

# Step 9.2 show balance function
def show_balance(balance):
    print('\n===== Balance Inquiry =====')
    print(f"Your Balance: {balance:.2f}")

# balance = get_balance('100001')
# show_balance(balance)

# STEP 10(Withdraw system) strat
# Step 10.1 select account type
def select_account_type(messages):
    while True:
        print(f'\n===== {messages['select_account_type']} =====')
        print(f'1.{messages['savings']}')
        print(f'2.{messages['current']}')
        
        choice = input('Select account type: ')
        if choice == '1':
            return 'Savings'
        elif choice == '2':
            return 'Current'
        else:
            print('Invalid choice. Please select 1 or 2.')

# account_type = select_account_type()
# print('Selected account type:', account_type)

# Create validate_account_type()
def validate_account_type(account_no, selected_type):
    account = get_account(account_no)
    if account is None:
        return False
    actual_type = account[4]
    return actual_type == selected_type

# Step 10.2 select withdraw amount
def select_withdraw_amount():
    while True:
        print('\n===== WITHDRAW AMOUNT =====')
        print('1. 500')
        print('2. 1000')
        print('3. 2000')
        print('4. 5000')
        print('5. Other')
        choice = input('Select amount: ')
        if choice == '1':
            return 500
        elif choice == '2':
            return 1000
        elif choice == '3':
            return 2000
        elif choice == '4':
            return 5000
        elif choice == '5':
            try:
                amount = float(input('Enter your amount: '))
                if amount > 0:
                    return amount
                print('Amount must be greater than 0.')
            except ValueError:
                print('Please enter a valid number.')
        else:
            print('Invalid choice. Please select 1-5.')

# amount = select_withdraw_amount()
# print('Your selected amount: ', amount)

# Step 10.3 validate withdraw function
def validate_withdrawal(balance, amount):
    if amount <= 0:
        return False
    if amount > balance:
        return False
    return True

# print(validate_withdrawal(100000, 5000))
# print(validate_withdrawal(100000, 150000))
# print(validate_withdrawal(100000, 00))

# Step 10.4 update balance function
def update_balance(account_no, new_balance):
    connection = sqlite3.connect('atm.db')
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE accounts
    SET balance = ?
    WHERE account_no = ?
    """, (new_balance, account_no,))

    connection.commit()

    connection.close()

    return True

# update_balance('100001', 150000)
# print(get_balance('100001'))

# Step 10.5 withdraw money function
def withdraw_money(account_no, amount):
    # fetch the data
    balance = get_balance(account_no)

    if balance is None:
        return None
    if not validate_withdrawal(balance, amount):
        return None
    new_balance = balance - amount
    update_balance(account_no, new_balance)
    return new_balance

# new_balance = withdraw_money('100001', 50000)
# print('New balance:', new_balance)
# print('Database balance:', get_balance('100001'))

# Step 10.6 Create save transaction function
def save_transaction(account_no, transaction_type, amount, balance_after):
    connection = sqlite3.connect('atm.db')
    cursor = connection.cursor()

    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("""
    INSERT INTO transactions 
    (account_no, transaction_type, 
    amount, balance_after, created_at)
    VALUES (?, ?, ?, ?, ?)
    """, (
        account_no, 
        transaction_type, 
        amount, 
        balance_after, 
        created_at
    ))

    connection.commit()
    connection.close()

    return True

# result = save_transaction('100001', 'withdraw', 5000, 95000)
# print(result)

# connection = sqlite3.connect('atm.db')
# cursor = connection.cursor()
# cursor.execute('SELECT * FROM transactions')
# transactions = cursor.fetchall()
# for transaction in transactions:
#     print(transaction)
# connection.commit()
# connection.close()

# Step 10.7 Create dispense cash function
def dispense_cash(amount):
    print('\nProcessing cash...')
    print(f"Dispensing {amount:.2f}...")
    print('Please take your cash.')
    return True

# result = dispense_cash(5000)
# print('Cash dispensed:', result)

# STEP 11 RECEIPT FUNCTIONALITY
# step 11.1 create ask for receipt function
def ask_for_receipt():
    while True:
        choice = input('\nDo you want a receipt? (y/n): ').lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Invalid choice. Please enter y or n.')

# receipt = ask_for_receipt()
# print('Receipt Requested:', receipt)

# Step 11.2 create print receipt function
def print_receipt(transaction):
    print('\n=========== ATM RECEIPT ============')
    print(f"Account No: {transaction['account_no']}")
    print(f"Transaction Type: {transaction['transaction_type']}")

    if transaction['transaction_type'] == 'Withdraw':
        print(f"Withdraw Ammount: {transaction['amount']:.2f}")
    elif transaction['transaction_type'] == 'Transfer Sent':
        print(f"Transfer Ammount: {transaction['amount']:.2f}")
    elif transaction['transaction_type'] == 'Balance Inquiry':
        print(f"Available Blance: {transaction['balance_after']:.2f}")
    print(f"Balance Now: {transaction['balance_after']:.2f}")
    print(f"Date and Time: {transaction['created_at']}")
    print('===============================')

# transaction = {
#     'account_no' : '100001',
#     'transaction_type' : 'Withdraw',
#     'amount' : 5000,
#     'balance_after' : 95000,
#     'created_at' : '2026-09-27 20:30:00'
# }
# print_receipt(transaction)

# STEP 12(Eject Card)
# create eject card function
def eject_card():
    print('\nPlease take ypur card.')
    print('Card ejected successfully.')
# eject_card()

# Complete ATM Flow Start Here
# Step 13.1 creat insert card function
def insert_card():
    print('\n====== INSERT CARD ======')
    account_no = input('Enter account number: ')
    return account_no


# STEP 14 Transfer functonality start
# Step 14.1 create get receiver account number function
def get_receiver_account():
    receiver_account_no = input('Enter receiver account number: ')
    return receiver_account_no
# receiver = get_receiver_account()
# print('Receiver no:', receiver)

# Step 14.2 creat verify_recevier()
def verify_recevier(account_no):
    account = get_account(account_no) # fetch account_no from get_account
    if account is None:
        return False
    return True

# Step 14.3 create validate_transfer()
def validate_transfer(balance, amount):
    if amount <= 0:
        return False
    if amount > balance:
        return False
    return True
# print(validate_transfer(100000, 5000))
# print(validate_transfer(100000, 150000))
# print(validate_transfer(100000, 000))

# Step 14.4 create transfer_money()
def transfer_money(sender_account_no, receiver_account_no, amount):
    sender_balance = get_balance(sender_account_no)
    receiver_balance = get_balance(receiver_account_no)
    if sender_balance is None or receiver_balance is None:
        return False
    if not validate_transfer(sender_balance, amount):
        return False

    new_sender_balance = sender_balance - amount
    new_receiver_balance = receiver_balance + amount

    update_balance(sender_account_no, new_sender_balance)
    update_balance(receiver_account_no, new_receiver_balance)

    save_transaction(
        sender_account_no,
        'transfer_sent',
        amount,
        new_sender_balance
    )
    save_transaction(
        receiver_account_no,
        'transfer_received',
        amount,
        new_receiver_balance
    )
    return True

# STEP 15 TRANSFER AMOUNT FUNCTIONALITY
# create get_transfer_amount()
def get_transfer_amount():
    while True:
        try:
            amount = float(input('Enter transfer amount: '))
            if amount <= 0:
                print('Amount must be greater than 0.')
                continue
            return amount
        except ValueError:
            print('Please enter a valid number.')
        

# # Main functionality start here
account_no = insert_card()
account = get_account(account_no)
if account is None:
    print('Account not found.')
else:
    show_language_menu()
    language = select_language()
    messages = load_language(language)
    # call the athenticate_user function
    account = athenticate_user(account_no, messages)
    if account is None:
        print('Athentication failed.')
    else:
        print(messages['welcome'].format(name=account[2]))

        # show_main_menu()
        # choice = get_menu_choice()
        atm_menu(account_no, messages)

