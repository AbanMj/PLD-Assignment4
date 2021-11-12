# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def UserInput():
    apple_pieces = int(input("Enter the pieces of apple/s you want: "))
    orange_pieces = int(input("Enter the pieces of orange/s you want: "))
    return apple_pieces, orange_pieces

def prices():
    apple_pr = 20
    orange_pr = 25
    return apple_pr, orange_pr

def calculation(apple_pr, apple, orange_pr, orange):
    priceF = (apple_pr*apple) + (orange_pr*orange)
    return priceF

def display(bill):
    print(f"The total amount is {bill}.")
# ask how many apple and orange you want to buy
apple, orange = UserInput()
# prices of apple and orange
apple_pr, orange_pr = prices()
# total amount you pay
bill = calculation(apple_pr, apple, orange_pr, orange)
display(bill)