variable=input("Enter a variable name:")
if variable[0].isalpha() or variable[0].startswith("_"):
    print("True")
else:
    print("False")