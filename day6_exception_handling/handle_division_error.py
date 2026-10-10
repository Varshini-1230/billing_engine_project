#Handle division errors
try:
    num1=int(input("Enter n1 value:"))
    num2=int(input("Enter n2 Value:"))
    div=num1/num2
except ValueError:
    print("The number should be Integer")
except ZeroDivisionError:
    print("The num2 should not be Zero")
else:
    print("Division of two numbers is :",div)
finally:
    print("Division is calculated")