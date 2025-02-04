# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the savings account balance: $"))
    savings_interest = float(input("Enter the savings account interest rate (in %): "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))

    # Call the create_savings_account function and pass the variables from the user.
    savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nInterest Earned on Savings Account over {savings_maturity} months: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Account Balance: ${savings_updated_balance:.2f}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter the CD account balance: $"))
    cd_interest = float(input("Enter the CD account interest rate (in %): "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))
    # Call the create_cd_account function and pass the variables from the user.
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Interest Earned on CD Account over {cd_maturity} months: ${cd_interest_earned:.2f}")
    print(f"Updated CD Account Balance: ${cd_updated_balance:.2f}\n")

if __name__ == "__main__":
    # Call tdef main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Define a function to get user input for account details
    def get_account_details(account_type):
        balance = float(input(f"Enter the {account_type} account balance: $"))
        interest = float(input(f"Enter the {account_type} account interest rate (in %): "))
        maturity = int(input(f"Enter the number of months for the {account_type} account: "))
        return balance, interest, maturity

    # Define a function to calculate and display interest earned
    def calculate_and_display_interest(account_type, balance, interest, maturity, updated_balance, interest_earned):
        print(f"\nInterest Earned on {account_type} Account over {maturity} months: ${interest_earned:.2f}")
        print(f"Updated {account_type} Account Balance: ${updated_balance:.2f}\n")

    # Get user input for savings account details
    savings_balance, savings_interest, savings_maturity = get_account_details("savings")

    # Call the create_savings_account function and pass the variables from the user
    savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Calculate and display interest earned for savings account
    calculate_and_display_interest("Savings", savings_balance, savings_interest, savings_maturity, savings_updated_balance, savings_interest_earned)

    # Get user input for CD account details
    cd_balance, cd_interest, cd_maturity = get_account_details("CD")

    # Call the create_cd_account function and pass the variables from the user
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Calculate and display interest earned for CD account
    calculate_and_display_interest("CD", cd_balance, cd_interest, cd_maturity, cd_updated_balance, cd_interest_earned)

if __name__ == "__main__":
    # Call the main function
    main()