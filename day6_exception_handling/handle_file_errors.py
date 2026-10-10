#Handle file errors
file_name=input("Enter file name:")
try:
    file=open(file_name,"r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not Found ")
except Exception as e:
    print(f"An Unexpected Error occured {e}")
    

