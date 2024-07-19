from csv_create import CSV
from data_entry import get_amount, get_category, get_date, get_description
from pandas import DataFrame

import matplotlib.pyplot as plt
import pandas as pd


def add() -> None:
    CSV.initialise_csv()

    date: str = get_date("Enter the date for the Transaction (dd-mm-yyyy) or enter for today's date: ",
                         True)

    amount: float = get_amount()

    category: str = get_category()

    description: str = get_description()

    CSV.add_entry(date, amount, category, description)


def get(start_date, end_date) -> DataFrame:
    return CSV.get_transactions(start_date, end_date)


def plot_transactions(df: DataFrame) -> None:
    df.set_index("date", inplace=True)

    income_df: DataFrame = df[df["category"] == "Income"].resample(
        "D").sum().reindex(pd.date_range(start=df.index.min(), end=df.index.max(), freq='D'), fill_value=0)
    
    expense_df: DataFrame = df[df["category"] == "Expense"].resample(
        "D").sum().reindex(pd.date_range(start=df.index.min(), end=df.index.max(), freq='D'), fill_value=0)
    
    
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()
