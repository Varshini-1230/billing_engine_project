file=open("students.txt",'w')
file.write("The 5 Student names are:\njohn\nravi\nrahul\nkeerthi\nsujana\n")
file.close()

file=open('students.txt','r')
content=file.read()
print(content)