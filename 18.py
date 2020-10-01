'''Program to print the sum of (1/2)+(1/4)+(1/6).............(1/n)
Developer:Aakash
Date:03.03.2020
--------------------------------'''
a=int(input("Enter the number for which you want sum up="))
j=2
sm=0;
while(j<=a):
    sm=sm+(1/j)
    j=j+2
print("The desired sum is=",sm)

