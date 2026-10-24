#Handle invalid number input
try:
    n1=int(input())
    n2=int(input())
    sum=n1+n2
    
except ValueError:
    print("The input is invalid")
else:
    print("Successfully calculates sum")
    print("Sum:",sum)