file=open("20_students.txt","w")
file.write("varshini\nrahul\nrani\nseeta\ngeeta\n")
file.close()

file=open("20_students.txt",'r')
for i in range(5):
    name=file.readline().strip()
    print(i+1,name)