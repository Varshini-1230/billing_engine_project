file=open("12_create_number.txt",'w')
file.write("1\n2\n3\n4\n6\n90\n32\n45")
file.close()

file=open("12_create_number.txt",'r')
content=file.read()
print(content)