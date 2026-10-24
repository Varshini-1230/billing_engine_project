import os
filename = input("Enter filename: ")
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted")

else:
    print("File not delete")