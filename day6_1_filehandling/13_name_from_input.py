
#Take 5 names from the user using input() and write them into a file.
file=open("13_names_from_input.txt",'w')
for name in range(5):
    names=input("Enter name:")
    file.write(names+"\n")


