import json
import os

DATAFILE = "data.json"

def load_data():
    if not os.path.exists(DATAFILE):
        initialbalance = float(input("Welcome! set your initial balance: "))
        data = {
            "balance": initialbalance,
            "transactions": []
        }
        save_data(data)
        return data
    else:
        with open(DATAFILE, "r") as f:
            return json.load(f)
    
def save_data(data):
    with open(DATAFILE, "w") as f:
        json.dump(data, f, indent=2)