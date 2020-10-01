'''Program to print the sum of (1/3)+(1/5)+(1/7).............(1/n)
Developer:Aakash
Date:03.03.2020
--------------------------------'''
a=int(input("Enter the number for which you want sum up="))
j=1
sm=0;
while(j<=a):
    sm=sm+(1/j)
    j=j+2
print("The desired sum is=",sm)

