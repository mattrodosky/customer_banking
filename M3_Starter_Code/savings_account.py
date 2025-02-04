"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Define a function for the Savings Account
def create_savings_account(savings_balance, savings_interest, savings_maturity):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    savings_account = Account(savings_balance, 0)
   
    # Calculate interest earned
    savings_interest_earned = savings_balance * (savings_interest/100 * savings_maturity/12)
    # Update the savings account balance by adding the interest earned
    savings_updated_balance = savings_balance + savings_interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    savings_account.set_balance(savings_updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    savings_account.set_interest(savings_interest_earned)
    # Return the updated balance and interest earned.
    return  savings_updated_balance, savings_interest_earned