filename = input("Enter filename: ")
try:
    file = open(filename, "x")
    print("File created successfully.")
    file.close()
except FileExistsError:
    print("File already exists.")