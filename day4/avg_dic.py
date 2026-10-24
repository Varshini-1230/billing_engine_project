d1={"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
tot=0
for mark in d1.values():
    tot+=mark
print("average:",tot/len(d1))