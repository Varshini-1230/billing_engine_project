file=open("10_numbers_min_max.txt",'w')
file.write("1\n2\n3\n4\n5\n6\n7\n")
file.close()

file=open("10_numbers_min_max.txt",'r')
content=file.read().split()
for num in content:
    num=int(num)
print("largest:",max(content))
print("Smallest:",min(content))
print()

print("Another approch")
#Another approach
file=open("10_numbers_min_max.txt",'w')
file.write("1\n2\n3\n4\n5\n6\n7\n")
file.close()

file=open("10_numbers_min_max.txt",'r')
content=file.read().split()
largest=content[0]
smallest=content[0]
for num in content:
    if num >largest:
        largest=num
    if num < smallest:
        smallest=num
print("Largest:",largest)
print("Smallest:",smallest)
    