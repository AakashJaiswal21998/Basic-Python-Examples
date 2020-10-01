'''Program to print the grading of student
Developer:Aakash
Date:21.02.2020
--------------------------------'''
a=int(input("Enter your Percentage="))
if(a<25):
    print("You are getting the grade 'F'")
elif(a<45 or a>25):
    print("You are getting the grade 'E'")
elif(a<50 or a>45):
    print("You are getting the grade 'D'")
elif(a<60 or a>50):
    print("You are getting the grade 'C'")
elif(a<80 or a>60):
    print("You are getting the grade 'B'")
elif(a>80):
    print("You are getting the grade 'A'")
else:
    print("Oops! You are not putting wrong value!")

