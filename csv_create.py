import pandas as pd
import csv

from datetime import datetime, date
from pandas import DataFrame, Series
from csv import DictWriter


class CSV:
    """class for working on csv files
    """
    CSV_FILE: str = "finance_data.csv"
    COLUMNS: list[str] = ["date", "amount", "category", "description"]
    FORMAT: str = "%d-%m-%Y"

    @classmethod
    def initialise_csv(cls) -> None:
        """initialization create the csv file
        """
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df: DataFrame = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date_entry: str, amount: float, category: str, description: str) -> None:
        """Add a new entry to the data list

        Args:
            date (date): date of the entry
            amount (int): amount of the entry
            category (str): category of the entry
            description (str): description
        """
        new_entry: dict = {
            "date": date_entry,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer: DictWriter = csv.DictWriter(
                csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)

        print("Entry Added Successfully!!!")

    @classmethod
    def get_transactions(cls, start_date: str, end_date: str) -> DataFrame:
        df = pd.read_csv(cls.CSV_FILE)

        df["date"] = pd.to_datetime(df["date"], format=cls.FORMAT)

        start_date_format: date = datetime.strptime(start_date, cls.FORMAT)

        end_date_format: date = datetime.strptime(end_date, cls.FORMAT)

        mask: Series[bool] = (df["date"] >= start_date_format) & (
            df["date"] <= end_date_format)

        filtered_df: DataFrame = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transactions from {start_date_format.strftime(
                cls.FORMAT)} to {end_date_format.strftime(cls.FORMAT)}\n")
            
            print(filtered_df.to_string(index=False, formatters={
                  "date": lambda x: x.strftime(cls.FORMAT)}))
            
            total_income: float = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense: float = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            
            print("\nSummary:")
            print(f"Total Income: {total_income:.2f}")
            print(f"Total Expense: {total_expense:.2f}")
            
            print(f"Net Savings: {(total_income - total_expense):.2f}")
            
        return filtered_df
            
