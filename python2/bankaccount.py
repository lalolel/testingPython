# Step 1: Create the BankAccount class
class BankAccount(object):
    # Step 2: Add a member variable called balance and set it to 0
    balance = 0
    
    # Step 3 & 4: Add the __init__ method that takes self and name parameters
    def __init__(self, name):
        # Assign the name parameter to the self.name property
        self.name = name
    
    # Step 5 & 6: Add a __repr__ method that returns account information
    def __repr__(self):
        # Return a formatted string with the account owner and balance
        return "This account belongs to {} and has ${:.2f}".format(self.name, self.balance)
    
    # Step 7 & 8: Add a show_balance method to display just the balance
    def show_balance(self):
        # Print the balance formatted to two decimal places
        print "Balance: ${:.2f}".format(self.balance)
    
    # Step 9, 10, 11, 12, & 13: Add a deposit method
    def deposit(self, amount):
        # Check if the amount is valid (greater than zero)
        if amount <= 0:
            print "Error: Cannot deposit zero or negative amount"
        else:
            # Print the amount deposited
            print "Depositing ${:.2f}".format(amount)
            # Increment the balance by the deposit amount
            self.balance += amount
            # Display the new balance by calling show_balance method
            self.show_balance()
    
    # Step 14, 15, 16, 17, & 18: Add a withdraw method
    def withdraw(self, amount):
        # Check if there's enough balance for the withdrawal
        if amount > self.balance:
            # Print error message if withdrawal amount exceeds balance
            print "Error: Cannot withdraw more than available balance"
        else:
            # Print the withdrawal amount
            print "Withdrawing ${:.2f}".format(amount)
            # Decrement the balance by the withdrawal amount
            self.balance -= amount
            # Display the new balance by calling show_balance method
            self.show_balance()


# Step 19: Create a BankAccount object
my_account = BankAccount("Alice")

# Step 20: Print the account object to test __repr__ method
print my_account

# Step 21: Call show_balance to display just the balance
my_account.show_balance()

# Step 22: Deposit 2000 dollars
my_account.deposit(2000)

# Step 23: Withdraw 1000 dollars
my_account.withdraw(1000)

# Step 24: Print the account object again to verify changes
print my_account

# Step 25: Run the program with: python bankaccount.py
