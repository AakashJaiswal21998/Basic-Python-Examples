'''Program to print the sum of 1-2+3+4-5+6-7.............n
Developer:Aakash
Date:03.03.2020
--------------------------------'''
a=int(input("Enter the number for which you want sum up="))
i=1;j=2
su=0;sm=0;
while(i<=a):
    su=su+i
    i=i+2
print("The odd sum is=",su)
while(j<=a):
    sm=sm+j
    j=j+2
print("The even sum is=",sm)
print("The desired sum is=",su-sm)
