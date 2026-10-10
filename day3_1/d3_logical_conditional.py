age=int(input("Enter age:"))
has_id =input("Enter person has Id or Not:").lower()
if age>=18 and has_id=="yes":
    print("Allowed")
else:
    print("Not Allowed")