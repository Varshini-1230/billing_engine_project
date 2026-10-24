file=open("8_even.txt",'w')
file.write("1\n2\n3\n4\n5\n6\n7\n8\n")
file.close()
file=open("8_even.txt",'r')
for num in file:
    num=int(num)
    if num %2==0:
        print(num)