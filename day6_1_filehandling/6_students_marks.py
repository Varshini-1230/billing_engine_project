import os 
file = open("6_student_marks_detail.txt","r")
name=file.readline()
age=file.readline()
marks=file.readline()
print(name,end="")
print(age,end="")
print(marks,end="")
file.close()