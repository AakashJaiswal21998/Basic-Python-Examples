'''Program to print the Bonus if Employee is spending more than 5 years
Developer:Aakash
Date:21.02.2020
--------------------------------'''
a=int(input("Enter your service year="))
if(a>5):
    print("You are elegible for Bonus!")
    b=int(input("You are salary="))
    c=(5/100)*b
    print("Your discount amount is=Rs",c)
else:
    print("Oops! You are not elegible for Bonus!")
