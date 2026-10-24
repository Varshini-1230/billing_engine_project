d1={"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}

print(max((d1.values())))
highest_name=""
highest_marks=0
for name,marks in d1.items():
    if marks>highest_marks:
        highest_marks=marks
        highest_name=name
print(f"the student {highest_name} has highest marks {highest_marks}")
print(highest_name)
print(highest_marks)
