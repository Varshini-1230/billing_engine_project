file=open("over_write.txt",'w')
file.write("hello \n Good morning \n")
file.close()

file=open("over_write.txt",'r')
content=file.read()
print(content)
file.close()
print()

file=open("over_write.txt",'w')
file.write("How are you?\nHave a nice day\n")
file.close()

file=open("over_write.txt",'r')
content=file.read()
print(content)
file.close()
print()