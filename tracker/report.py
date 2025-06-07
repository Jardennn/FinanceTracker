from . import logger

def show_report():
    try:   
        filepath = 'transactions.log'

        expensecount = 0
        incomecount = 0

        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                expensecount += line.upper().count("expense".upper())
    
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                incomecount += line.upper().count("income".upper())

        print(f"Total expenses: {expensecount}")
        print(f"Total income: {incomecount}")
    except FileNotFoundError:
        print("Log file doesn't exist or you just didn't submit any transactions!")