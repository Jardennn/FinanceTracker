from tracker import tracker, report, storage

def main():
    while True:
        data = storage.load_data()
        print("\n === Personal Finance Tracker ===")
        print(f"Your current balance: ₪{data['balance']:.2f}")
        print("Choose your option on what to do:")
        print("1) Add expense")
        print("2) Add income")
        print("3) Show report")
        print("4) Exit")
        choice = int(input("Choose an option (1-4): "))

        if choice == 1:
            print("------------------------------------")
            tracker.add_expense()
            print("------------------------------------")

        elif choice == 2:
            print("------------------------------------")
            tracker.add_income()
            print("------------------------------------")
        
        elif choice == 3:
            print("------------------------------------")
            report.show_report()
            print("------------------------------------")
        
        elif choice == 4:
            print("Goodbye!")
            break
        
        else:
            print('Invalid answer, try again.')
            print('-------------------------------------------')

if __name__ == "__main__":
    main()