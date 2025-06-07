from . import storage
from . import logger

def add_expense():
    # Prompts for data
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category: ")
    date = input("Enter the date of expense (DD/MM/YYYY): ")

    # Load existing data and append the new expense
    data = storage.load_data()
    data['transactions'].append({
        "type": 'expense',
        'amount': amount,
        'category': category,
        'data': date
    })

    
    data['balance'] -= amount

    storage.save_data(data)
    logger.log_trans("expense", amount, category, date)
    print("Expense added!")
    print(f"Your current balance: {data['balance']}")

def add_income():
    # Prompts for data
    amount = float(input("Enter the amount earned: "))
    source = input("Enter the source of income: ")
    date = input("Enter the date of income (DD/MM/YYYY): ")

    data = storage.load_data()
    data['transactions'].append({
        "type": 'income',
        'amount': amount,
        'source': source,
        'date': date
    })

    data['balance'] += amount
    
    storage.save_data(data)
    logger.log_trans("income", amount, source, date)
    print("Income added!")
    print(f"Your current balance: {data['balance']}")