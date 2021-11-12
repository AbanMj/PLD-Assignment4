# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def UserInput():
    moneyF = int(input("Amount of money you have:"))
    apple_pr = int(input("The price of an apple: "))
    return moneyF, apple_pr

def computeF(moneyF, apple_pr):
    amount_apple = moneyF // apple_pr
    change = moneyF % apple_pr
    return amount_apple, change

def display(amount_apple, change):
    print(f"You can buy {amount_apple} apples and your change is {change} pesos.")

# amount of money you have and price of the apple
money, apple_pr = UserInput()
# Number of apple you can buy and your remaining money
amount_apple, change = computeF(money, apple_pr)
#display
display(amount_apple, change)