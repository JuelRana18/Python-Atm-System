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

# STEP 6
# Athenticate_user function
def authenticate_user(account_no, messages):
    # call get_account() for filter account_no
    account = get_account(account_no)
    if account is None:
        print(messages['account_not_found'])
        return None
    entered_pin = input(messages['enter_pin'])
    if verify_pin(account_no, entered_pin):
        return account
    else:
        print(messages['invalid_pin'])
        return None


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


def load_language(language):
    if language == 'Bangla':
        return {
            # account
            'authentication_failed': 'অনুমোদন ব্যর্থ হয়েছে।',
            'welcome': 'ATM এ স্বাগতম,{name}!', 
            'enter_pin': 'PIN দিন: ',
            'invalid_pin': 'ভুল PIN',
            'balance': 'আপনার ব্যালেন্স',
            'account_not_found':'একাউন্ট পাওয়া যায়নি',

            # get menu choice
            'select_option': 'একটি অপশন নির্বাচন করুন: ',
            'invalid_menu_choice': 'ভুল নির্বাচন। ১-৪এর মধ্যে নির্বাচন করুন।',

            # show main menu
            'withdraw': 'টাকা উত্তোলন',
            'balance_inquiry':'ব্যালান্স দেখুন',
            'transfer': 'ট্রান্সফার',
            'exit': 'বের হয়ে যান',
            'atm_menu': 'ATM মেনু',

            # select account type
            'select_account_type': 'একাউন্টের ধরণ নির্বাচন করুন: ',
            'savings': 'সেভিংস',
            'current': 'কারেন্ট',
            'invalid_account_type': 'একাউন্ট টাইপ ভুল, ১ অথবা ২ টাইপ করুন। ',

            # amount selection withdraw
            'withdraw_amount': 'উত্তোলনের পরিমাণ নির্বাচন করুন',
            'other': 'অন্যান্য',
            'enter_amount': 'টাকার পরিমাণ লিখুন: ',
            'invalid_choice': 'ভুল নির্বাচন।অনুগ্রহ করে ১-৫এর মধ্যে নির্বাচন করুন।',
            'amount_positive': 'টাকার পরিমাণ শূন্যের বেশি হতে হবে।',
            'valid_number': 'অনুগ্রহ করে একটি সঠিক সংখ্যা লিখুন।',
            'amount': 'টাকার পরিমাণ',
            'processing': 'প্রক্রিয়া চলছে ....',

            # validation and successful withdraw
            'insufficient_balance': 'পর্যাপ্ত  ব্যালান্স নেই।',
            'withdraw_successful': 'টাকা উত্তোলন সফল হয়েছে।',
            'withdraw_failed': 'টাকা উত্তোলন সফল হয়নি ',
            'cash_processing': 'টাকা প্রক্রিয়াকরণ চলছে ...',

            # dispensing
            'dispensing': 'টাকা দেওয়া হচ্ছে: {amount:.2f}...',
            'take_cash': 'অনুগ্রহ করে টাকা নিন।',

            # balance inquiry
            'balance_title': 'ব্যালেন্স অনুসন্ধান',
            'your_balance': 'আপনার ব্যালেন্স: {balance:.2f}',
            'balance_not_available': 'আপনার ব্যালেন্স পাওয়া যায়নি।',

            # ask for receipt
            'receipt_prompt': 'আপনি কি রশিদ চান ? (y/n): ',
            'invalid_yes_no': 'ভুল নির্বাচন। y অথবা n দিন।',

            # transfer
            'transfer_amount_display': 'ট্রান্সফারের পরিমাণ: {amount:.2f}',
            'receiver_account': 'প্রাপকের একাউন্ট নম্বর দিন: ',
            'receiver_verified': 'প্রাপক যাচাই সফল হয়েছে।',
            'transfer_amount': 'ট্রান্সফারের পরিমান লিখুন: ',
            'transfer_successful': 'ট্রান্সফার সফল হয়েছে।',

            # transfer erorr
            'self_transfer_not_allowed': 'নিজের একাউন্টে টাকা ট্রান্সফার করা যাবে না।',
            'receiver_not_found': 'প্রাপকের একাউন্ট পাওয়া যায়নি।',
            'transfer_failed': 'ট্রান্সফার ব্যর্থ হয়েছে।',
            'transfer_insufficient': 'ট্রান্সফারের জন্য পর্যাপ্ত ব্যালেন্স নেই।',
            'transfer_amount_positive': 'ট্রান্সফারের পরিমাণ শূন্যের চেয়ে বেশি হতে হবে।',
            'transfer_valid_number': 'সঠিক সংখ্যা লিখুন।',

            # receipt
            'receipt_title': 'ATM রশিদ',
            'account_no': 'একাউন্ট নম্বর',
            'transaction_type': 'লেনদেনের ধরণ',
            'withdraw_amount_label': 'উত্তোলনের পরিমাণ',
            'transfer_amount_label': 'ট্রান্সফারের পরিমাণ',
            'available_balance': 'পর্যাপ্ত ব্যালেন্স',
            'balance_now': 'বর্তমান ব্যালেন্স',
            'date_time': 'তারিখ ও সময়',

            # Exit and card eject
            'exit_selected': 'বের হওয়া নির্বাচিত করা হয়েছে।',
            'take_card': 'অনুগ্রহ করে আপনার কার্ডটি নিন।',
            'card_ejected': 'সফলভাবে কার্ড বের করা হয়েছে।',
            
        }
    elif language == 'English':
        return {
            # account
            'authentication_failed': 'Authentication failed.',
            'welcome': 'Welcome to ATM,{name}!',
            'enter_pin': 'Enter PIN: ',
            'invalid_pin': 'Invalid PIN',
            'balance': 'Your balance',
            'account_not_found': 'Account not found.',

            # get menu choice
            'select_option': 'Select an option: ',
            'invalid_menu_choice': 'Invalid choice. Please select 1-4.',

            # show main menu
            'withdraw': 'Withdraw ',
            'balance_inquiry':'Balance Inquiry',
            'transfer': 'Transfer',
            'exit': 'Exit',
            'atm_menu': 'ATM MENU',

            # select account type
            'select_account_type': 'Select Account Type: ',
            'savings': 'Savings',
            'current': 'Current',
            'invalid_account_type': 'Invalid Account Type, type 1 or 2.',

            # amount selection
            'withdraw_amount': 'Select Withdraw Amount',
            'other': 'Other',
            'enter_amount': 'Enter Amount: ',
            'invalid_choice': 'Invalid Choice. Please Select 1-5.',
            'amount_positive' : 'Amount Must Be Greater Than 0.',
            'valid_number': 'Please Enter A Valid Number.',
            'amount': 'Amount',
            'processing': 'Processing ...',

            # validation and successful withdraw
            'insufficient_balance': 'Insufficient balance.',
            'withdraw_successful': 'Withdraw successful.',
            'withdraw_failed': 'Withdraw failed.',
            'cash_processing': 'Processing cash ...',

            # dispensing
            'dispensing': 'Dispensing: {amount:.2f}...',
            'take_cash': 'Please take your cash.',

            # balance inquiry
            'balance_title': 'BALANCE INQUIRY',
            'your_balance': 'Your balance: {balance:.2f}',
            'balance_not_available': 'Your balance not available.',

            # ask for receipt
            'receipt_prompt': 'Do you want a receipt ? (y/n): ',
            'invalid_yes_no': 'Invalid choice. Please enter y or n.',

            # transfer
            'transfer_amount_display': 'Transfer amount: {amount:.2f}',
            'receiver_account': 'Enter receiver account number: ',
            'receiver_verified': 'Receiver verified.',
            'transfer_amount': 'Enter transfer amount: ',
            'transfer_successful': 'Transfer successful.',

            # transfer erorr
            'self_transfer_not_allowed': 'You can not transfer money to your own account.',
            'receiver_not_found': 'Receiver account not found.',
            'transfer_failed': 'Transfer failed.',
            'transfer_insufficient': 'Insufficient balance for transfer.',
            'transfer_amount_positive': 'Amount must be greater than 0.',
            'transfer_valid_number': 'Please enter a valid number.',

            # receipt
            'receipt_title': 'ATM RECEIPT',
            'account_no': 'Account No',
            'transaction_type': 'Transaction Type',
            'withdraw_amount_label': 'Withdraw Amount',
            'transfer_amount_label': 'Transfer Amount',
            'available_balance': 'Available Balance',
            'balance_now': 'Balance Now',
            'date_time': 'Date & Time', 

            # Exit and card eject
            'exit_selected': 'Exit selected.',
            'take_card': 'Please take your card.',
            'card_ejected': 'Card ejected successfully.',
            
        }
    elif language == 'Malay':
        return {

            # account
            'authentication_failed': 'Pengesehan gagal',

            'welcome': 'Salamat datang ke ATM,{name}!',
            'enter_pin': 'Masukkan PIN: ',
            'invalid_pin': 'PIN tidak sah',
            'balance': 'Baki anda',
            'account_not_found': 'Akaun tidak de jumpai',

            # get menu choice
            'select_option': 'Pilih satu pilihan: ',
            'invalid_menu_choice': 'Pilihan tidak sah. Sila pilih 1-4.',

            # show main menu
            'withdraw': 'Pengeluaran',
            'balance_inquiry':'Semakan Baki',
            'transfer': 'Pemindahan',
            'exit': 'Keluar',
            'atm_menu': 'MENU ATM',

            # select account type
            'select_account_type': 'Pilih Jenis Akaun: ',
            'savings': 'Simpanan',
            'current': 'Semasa',
            'invalid_account_type': 'Jenis akaun Tidak Sah, jenis 1 atau 2.',

            # amount selection
            'withdraw_amount': 'Pilih Jumla Pengeluaran.',
            'other': 'Lain-lain.',
            'enter_amount': 'Masukan Jumlah: ',
            'invalid_choice': 'Pilihan Tidak Sah. Sila Pilih 1-5.',
            'amount_positive': 'Jumlah Mestilah Lebih Daripada 0.',
            'valid_number': 'Sila Masukkan Nombor Yang Sah.',
            'amount': 'Jumlah',
            'processing': 'Sedang diproses ...',

            # validation and successful withdraw
            'insufficient_balance': 'Baki tidak mencukupi.',
            'withdraw_successful': 'Pengeluaran berjaya',
            'withdraw_failed': 'Pengeluaran tidak berjaya',
            'cash_processing': 'Tunai sedang diproses ...',

            # dispensing
            'dispensing': 'Mengeluarkan: {amount:.2f}...',
            'take_cash': 'Sila ambilwang tunai anda.',

            # balance inquiry
            'balance_title': 'SEMAKAN BAKI',
            'your_balance': 'Baki anda: {balance:.2f}',
            'balance_not_available': 'Baki anda tidak ditemui.',

            # ask for receipt
            'receipt_prompt': 'Adakan anda mahu resit ? (y/n): ',
            'invalid_yes_no': 'Pilihan tidak sah. Sila masukkan y atau n.',

            # transfer
            'transfer_amount_display': 'Jumlah pemindahan: {amount:.2f}',
            'receiver_account': 'Masukkan nombor akaun penerima: ',
            'receiver_verified': 'Penerima telah disahkan.',
            'transfer_amount': 'Masukkan jumlah pemindahan: ',
            'transfer_successful': 'Pimindahan barjaya.',

            # transfer erorr
            'self_transfer_not_allowed': 'Anda tidak boleh memidahkan wang ke akaun sendiri.',
            'receiver_not_found': 'Akaun penerima tidak sah dijumpai.',
            'transfer_failed': 'Pemindahan gagal.',
            'transfer_insufficient': 'Baki tidak mencukupi untuk pemindahan',
            'transfer_amount_positive': 'Jumlah mestilah lebih daripada 0.',
            'transfer_valid_number': 'Sila masukkan nomboryang sah.',

            # receipt
            'receipt_title': 'RESIT ATM',
            'account_no': 'Akaon Nombor',
            'transaction_type': 'Jenis Transaksi',
            'withdraw_amount_label': 'Jumlah Pengeluaran',
            'transfer_amount_label': 'Jumlah Pemindahan',
            'available_balance': 'Baki Tersedia',
            'balance_now': 'Baki Semesa',
            'date_time': 'Tarikh dan masa',

            # Exit and card eject
            'exit_selected': 'Keluar dipilih.',
            'take_card': 'Sila ambil kad anda.',
            'card_ejected': 'Kad berjaya dikeluarkan.'
        }
    else:
        return None

# STEP 8.1 --show_main_menu()
def show_main_menu(messages):
    print(f'\n===== {messages['atm_menu']} =====')
    print(f'1.{messages['withdraw']}')
    print(f'2.{messages['balance_inquiry']}')
    print(f'3.{messages['transfer']}')
    print(f'4.{messages['exit']}')
    

# get menu choice by user
def get_menu_choice(messages):
    while True:
        choice = input(messages['select_option'])
        if choice in ['1', '2', '3', '4',]:
            return choice
        print(messages['invalid_menu_choice'])


# STEP 15 Main Menu Loop Functionality
# Create atm_menu()
def atm_menu(account_no, messages):
    while True:
        show_main_menu(messages)
        choice = get_menu_choice(messages)
        if choice == '1':
            account_type = select_account_type(messages)
            if not validate_account_type(account_no, account_type):
                print(messages['invalid_account_type'])
                continue
            amount = select_withdraw_amount(messages)

            new_balance = withdraw_money(account_no, amount)
            if new_balance is None:        
                print(messages['withdraw_failed'])
            else:
                save_transaction(account_no, 'withdraw', amount, new_balance)
                dispense_cash(amount, messages)
                print(messages['withdraw_successful'])
                print(f"{messages['balance_now']}: {new_balance:.2f}")
                if ask_for_receipt(messages):
                    transaction = { 
                        'account_no': account_no,
                        'transaction_type': 'Withdraw',
                        'amount': amount,
                        'balance_after': new_balance,
                        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    print_receipt(transaction, messages)

        elif choice == '2':
            balance = get_balance(account_no)
            if balance is not None:
                show_balance(balance, messages)
                
                if ask_for_receipt(messages):
                    transaction = {
                        'account_no': account_no,
                        'transaction_type': 'Balance Inquiry',
                        'amount': 0,
                        'balance_after': balance,
                        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    print_receipt(transaction, messages)
            else:
                print(messages['balance_not_available'])
            
        elif choice == '3':
            receiver_account_no = get_receiver_account(messages)
            if  account_no == receiver_account_no:
                print(messages['self_transfer_not_allowed'])
            elif verify_receiver(account_no, receiver_account_no):
                print(messages['receiver_verified'])
    
                amount = get_transfer_amount(messages)
                print(messages['transfer_amount_display'].format(amount=amount))
    
                balance = get_balance(account_no)
                if validate_transfer(balance, amount):
                    result = transfer_money(
                        account_no,
                        receiver_account_no,
                        amount
                    )
                    if result:
                        print(messages['transfer_successful'])
                        if ask_for_receipt(messages):
                            transaction = {
                                'account_no': account_no,
                                'transaction_type': 'Transfer Sent',
                                'amount': amount,
                                'balance_after': get_balance(account_no),
                                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            }
                            print_receipt(transaction, messages)
                    else:
                        print(messages['transfer_failed'])
                else:
                    print(messages['insufficient_balance'])
            else:
                print(messages['receiver_not_found'])
        elif choice == '4':
            print(messages['exit_selected'])
            eject_card(messages)
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
def show_balance(balance, messages):
    print(f'\n====== {messages['balance_title']} ======')
    print(messages['your_balance'].format(balance=balance))


# STEP 10(Withdraw system) strat
# Step 10.1 select account type
def select_account_type(messages):
    while True:
        print(f'\n===== {messages['select_account_type']} =====')
        print(f'1.{messages['savings']}')
        print(f'2.{messages['current']}')
        
        choice = input(messages['select_account_type'])
        if choice == '1':
            return 'Savings'
        elif choice == '2':
            return 'Current'
        else:
            print(messages['invalid_account_type'])

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
def select_withdraw_amount(messages):
    while True:
        print(f'\n======= {messages['withdraw_amount']} =======')
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
                amount = float(input(messages['enter_amount']))
                if amount > 0:
                    return amount
                print(messages['amount_positive'])
            except ValueError:
                print(messages['valid_number'])
        else:
            print(messages['invalid_choice'])


# Step 10.3 validate withdraw function
def validate_withdrawal(balance, amount):
    if amount <= 0:
        return False
    if amount > balance:
        return False
    return True

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

# Step 10.7 Create dispense cash function
def dispense_cash(amount, messages):
    print(f'\n{messages['cash_processing']}')
    print(messages['dispensing'].format(amount=amount))
    print(messages['take_cash'])
    return True

# STEP 11 RECEIPT FUNCTIONALITY
# step 11.1 create ask for receipt function
def ask_for_receipt(messages):
    while True:
        choice = input(f'\n{messages['receipt_prompt']}').lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print(messages['invalid_yes_no'])

# Step 11.2 create print receipt function
def print_receipt(transaction, messages):
    print(f'\n====== {messages['receipt_title']} ======')
    print(f"{messages['account_no']}: {transaction['account_no']}")
    print(f"{messages['transaction_type']}: {transaction['transaction_type']}")

    if transaction['transaction_type'] == 'Withdraw':
        print(f"{messages['withdraw_amount_label']}: {transaction['amount']:.2f}")
    elif transaction['transaction_type'] == 'Transfer Sent':
        print(f"{messages['transfer_amount_label']}: {transaction['amount']:.2f}")
    elif transaction['transaction_type'] == 'Balance Inquiry':
        print(f"{messages['available_balance']}: {transaction['balance_after']:.2f}")
    print(f"{messages['balance_now']}: {transaction['balance_after']:.2f}")
    print(f"{messages['date_time']}: {transaction['created_at']}")
    print('===============================')

# STEP 12(Eject Card)
# create eject card function
def eject_card(messages):
    print(f'\n{messages['take_card']}')
    print(messages['card_ejected'])

# Complete ATM Flow Start Here
# Step 13.1 creat insert card function
def insert_card():
    print(f'\n====== INSERT CARD ======')
    account_no = input('Enter Account Number: ')
    return account_no


# STEP 14 Transfer functonality start
# Step 14.1 create get receiver account number function
def get_receiver_account(messages):
    receiver_account_no = input(messages['receiver_account'])
    return receiver_account_no

# Step 14.2 creat verify_receiver()
def verify_receiver(sender_account_no, receiver_account_no):
    if sender_account_no == receiver_account_no:
        return False
    account = get_account(receiver_account_no) # fetch account_no from get_account
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
def get_transfer_amount(messages):
    while True:
        try:
            amount = float(input(messages['transfer_amount']))
            if amount <= 0:
                print(messages['transfer_amount_positive'])
                continue
            return amount
        except ValueError:
            print(messages['transfer_valid_number'])
        

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
    account = authenticate_user(account_no, messages)
    if account is None:
        print(messages['authentication_failed'])
    else:
        print(messages['welcome'].format(name=account[2]))

        atm_menu(account_no, messages)
