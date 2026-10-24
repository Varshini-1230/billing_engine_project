file=open("14_score_above_50.txt",'w')
for i in range(4):
    name=input("Enter name:")
    marks=int(input("Enter marks:"))
    file.write(name+" "+str(marks)+"\n")
file.close()

file=open("14_score_above_50.txt",'r')
for line in file:
    name,marks=line.split()
    if int(marks) >=50:
        print(name,marks)
file.close()
