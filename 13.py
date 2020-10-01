'''Program to print the leap year
Developer:Aakash
Date:24.02.2020
--------------------------------'''
year=int(input("Enter the year="))
if((year%400 == 0)or((year%4 == 0)and(year%100!= 0))):
    print("You are entering a leap year")
else:
    print("Oops! You are not entering a leap year!")
