students_marks={
    "rani":78,
    "raju":65,
    "seeta":90,
    "John":87,
    "Vaish":90
}
print(max((students_marks.values())))
highest_name=""
highest_marks=0
for name,marks in students_marks.items():
    if marks>highest_marks:
        highest_marks=marks
        highest_name=name
print(f"the student {highest_name} has highest marks {highest_marks}")
print(highest_name)
print(highest_marks)