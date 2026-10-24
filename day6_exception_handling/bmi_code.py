#height=float(input())
#weight=int(input())
try:
    height=float(input("enter the height in float: "))
    weight=int(input("enter the weight in integer: "))
    bmi=weight/(height**2)
except ValueError:
    print("invalid data value type")
else:
    print(f"BMI Value:",{bmi})
finally:
    print("bmi is calculated")