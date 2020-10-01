'''Program to print the discount if the CP is greater than 1000
Developer:Aakash
Date:21.02.2020
--------------------------------'''
a=int(input("Enter your CP="))
if(a>1000):
    print("You are elegible for Discount!")
    b=(10/100)*a
    print("Your discount amount is=Rs",b)
else:
    print("Oops! You are not elegible for Discount!")

