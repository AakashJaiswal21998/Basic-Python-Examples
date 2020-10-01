'''Program to print the greater number between two number
Developer:Aakash
Date:21.02.2020
--------------------------------'''
a=int(input("Enter the number of classes held="))
b=int(input("Enter the number of classes attendant="))
c=((b/a)*100)
if(c>75):
    print("The student is elegible for exam and having attendance=",c,"%")
else:
    print("The student is not elegible for exam")
