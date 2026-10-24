import os
import sys
import datetime
import math
print(math.sqrt(16))
print(math.ceil(5.0))
print(math.floor(5.9))
print(math.factorial(5))

from datetime import datetime
now=datetime.now()
print(now)

from pathlib import Path 
files=Path(".").glob("*.py")
for file in files:      
    print(file)

print(sys.argv)

from collections import Counter
a=[1,2,3,4,4,5,6]
print(Counter(a))


import sqlite3
connection=sqlite3.connect("students.db")
cursor=connection.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS students (
                   id INTEGER, 
                   name Text
)
""")

connection.commit()
connection.close()
