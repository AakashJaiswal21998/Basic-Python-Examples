'''Program to print working area
Developer:Aakash
Date:24.02.2020
--------------------------------'''
age=int(input("Enter your age="))
sex=(input("Enter your sex="))
mar=(input("Enter your marital status="))
if(sex=='F'or sex=='f'):
    print("She is only work in 'Urban' areas")
elif((sex=='M'or sex=='m')and(age<=40 and age>=20)):
     print("He will work in any area")
elif((sex=='M'or sex=='m')and(age<=60 and age>=40)):
     print("He will work in 'Urban' area")
else:
    print("Please! contact to your schedular")
