#Append to an existing file
file=open("notes.txt",'w')
file.write("hello \n Good morning \n")
file.close()

file=open("notes.txt",'r')
content=file.read()
print(content)
file.close()
print()

file=open("notes.txt","a")
file.write("this the appended content")
file.close()

file=open("notes.txt",'r')
content=file.read()
print(content)
file.close()
print()