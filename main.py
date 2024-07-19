from logic import add, get, get_date, plot_transactions
from pandas import DataFrame

def main() -> None:
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary report within a date range")
        print("3. Exit")
        
        choice: str = input("Enter your choice (1-3): ")
        
        
        if choice == "1":
            add()
        elif choice == "2":
            start_date: str = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date: str = get_date("Enter the end date (dd-mm-yyyy): ")
            
            df: DataFrame = get(start_date, end_date)
            
            if input("Do you want to see a plot? (y/n): ").lower() == "y":
                plot_transactions(df)
                
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, Enter 1, 2 or 3.")
            
            
if __name__ == "__main__":
    main()