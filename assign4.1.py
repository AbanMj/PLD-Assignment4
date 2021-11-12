# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

def AllInfo():
    name_ = input("Enter your Name: ")
    age_ = int(input("Enter your Age: "))
    address_ = input("Enter your Address: ")
    return name_, age_, address_

def display(name_, age_, address_):
    print(f"Hi, my name is {name_}. I am {age_} years old and I live in {address_}.")
#step 1: ask for name, age, address
name, age, address = AllInfo()
#step 2: display
display(name, age, address) 
