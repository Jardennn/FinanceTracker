from datetime import datetime

def log_trans(transaction_type, amount, category_or_source, date):
    with open('transactions.log', 'a') as logfile:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logfile.write(f"Submitted on {timestamp} | Type: {transaction_type.upper()} | amount: {amount} | Category/Source: {category_or_source} | Date: {date}\n")