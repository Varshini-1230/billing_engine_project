#
#Append multiple lines
file=open("notes1.txt",'w')
file.write("varsh\njanu\nsrija\n")
file.close()

file=open("notes1.txt",'r')
content=file.read()
print(content)
file.close()
print()

num=int(input("Enter no.of students:"))
file=open("notes1.txt",'a')
for i in range(num):
    names=input()
    file.write(names+"\n")
file.close()
print()
file=open("notes1.txt",'r')
content=file.read()
print(content)
    