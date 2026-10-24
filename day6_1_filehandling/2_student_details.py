import os
file=open("2_students.txt","w")
file.write("varshini\nrahul\nrani\nseeta\ngeeta\n")
file.close()
file=open("2_students.txt","r")
content=file.readlines()
for line in content:
    line=line.strip()
    print(line)
    