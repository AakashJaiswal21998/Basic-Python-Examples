'''Program to print the sum of (x^1/1)+(x^2/2)+(x^3/3)+(x^4/4).............(x^n/n)
Developer:Aakash
Date:03.03.2020
--------------------------------'''
a=int(input("Enter the number for which you want sum up="))
x=int(input("Enter the value of x(numerator)="))
j=1
sm=0;
while(j<=a):
    sm=sm+((x**j)/j)
    j=j+1
print("The desired sum is=",sm)

