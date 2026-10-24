#Create a file containing several names. Read the file using a for loop and count how many names are present.
file=open("18_count_names.txt","w")
file.write("varshini\nrahul\nrani\nseeta\ngeeta\n")
file.close()

file=open("18_count_names.txt","r")
#content=file.read()
count=0
for name in file:
    count+=1
print("The count of names :",count)