#
#Take 5 numbers from the user and write them into a file, one number per line.
file=open("14_number_from_user.txt",'w')
for i in range(5):
    num=int(input("Enter numbers:"))
    file.write(str(num)+"\n")