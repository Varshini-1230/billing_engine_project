import os
file=open("4_number_sum.txt",'w')
file.write("1\n2\n3\n4\n5")
file.close()
file=open("4_number_sum.txt",'r')
content=file.readlines()
print(content)
total=0
for num in content:
    total+=int(num)
print(total)