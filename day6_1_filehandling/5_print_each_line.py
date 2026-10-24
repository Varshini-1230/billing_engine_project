import os
file=open("5_print_eachline.txt",'w')
file.write("hello\nGood Morning\n Everyone")
file.close()
file=open("5_print_eachline.txt",'r')
print(file.readline())
print(file.readline())
print(file.readline())
# print(content)
# for line in content:
#     print(line)