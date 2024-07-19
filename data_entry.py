from datetime import datetime


date_format: str = "%d-%m-%Y"

CATEGORIES: dict = {
    "I": "Income",
    "E": "Expense"
}

def get_date(prompt: str, allow_default: bool = False) -> str:
    """get date from user

    Args:
        prompt (str): prompt to user
        allow_default (bool, optional): check default date. Defaults to False.

    Returns:
        str: Returns a date string
    """    
    date_str: str = input(prompt)
    
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date: datetime = datetime.strptime(date_str, date_format)
        
        return valid_date.strftime(date_format)
    
    except ValueError:
        
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        
        return get_date(prompt, allow_default)
    


def get_amount() -> float:
    """Get amount from the user

    Raises:
        ValueError: Raise if the amount is not valid

    Returns:
        float: Return the amount
    """    
    try:
        amount: float = float(input("Enter the amount: "))
        
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        
        return amount
    
    except ValueError as e:
        print(e)
        
        return get_amount()
    

def get_category() -> str:
    category: str = input("Enter the category ('I' for income or 'E' for expense): ").upper()
    
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income or 'E' expense")
    return get_category()
    

def get_description() -> str:
    return input("Enter description (Optional): ")