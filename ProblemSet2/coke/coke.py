# In a file called coke.py, implement a program that prompts the user to 
# insert a coin, one at a time, each time informing the user of the amount 
# due. Once the user has inputted at least 50 cents, output how many 
# cents in change the user is owed. Assume that the user will only input 
# integers, and ignore any integer that isn’t an accepted denomination.

# Variable to keep track
amount_due = 50

# Loop until amount is greater than 0
while amount_due > 0:

    # Print the amount due
    print("Amount Due: ", amount_due)

    # Ask user to insert coin
    coin = int(input("Insert Coin: "))

    # Check if coin is 25, 10 or 5 cents
    if coin in [25, 10, 5]:
        # Substract value from amount_due
        amount_due -= coin

# Calculate change owed
change_owed = abs(amount_due)

# Print change owed
print("Change Owed: ", change_owed)
