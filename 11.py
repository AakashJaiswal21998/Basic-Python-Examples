'''Program to print the greater age between three people
Developer:Aakash
Date:21.02.2020
--------------------------------'''
a=int(input("Enter the age of first person="))
b=int(input("Enter the age of second person="))
c=int(input("Enter the age of third person="))
if(a>b):
    if(a>c):
        print("The first person you have entered is oldest among all i.e.,",a)
    else:
        print("The third person you have entered is oldest among all i.e.,",c)
elif(b>a):
     if(b>c):
        print("The second person you have entered is oldest among all i.e.,",b)
     else:
        print("The third person you have entered is oldest among all i.e.,",c)
else:
    print("The third person you have entered is oldest among all i.e.,",c)

if(a<b):
    if(a<c):
        print("The first person you have entered is youngest among all i.e.,",a)
    else:
        print("The third person you have entered is youngest among all i.e.,",c)
elif(b<a):
     if(b<c):
        print("The second person you have entered is youngest among all i.e.,",b)
     else:
        print("The third person you have entered is youngest among all i.e.,",c)
else:
    print("The third person you have entered is youngest among all i.e.,",c)

