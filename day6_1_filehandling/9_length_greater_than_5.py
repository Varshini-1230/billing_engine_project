file=open("2_students.txt",'r')
#content=file.read()
for name in file :
    if len(name)>5:
        print(name)