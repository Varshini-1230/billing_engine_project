file=open("17_number_avg.txt",'w')
file.write("1\n2\n3\n4\n5")
file.close()

file=open("17_number_avg.txt",'r')
tot=0
count=0
for num in file:
    num=int(num)
    tot+=num
    count+=1
print("The average:",tot/count)