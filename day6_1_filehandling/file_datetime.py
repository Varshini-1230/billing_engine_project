file=open("practice2.py",'w')
file.write("from datetime import datetime\n"
"now=datetime.now()\n"
"print(now)")
file.close()

file=open("practice2.py",'r')
content=file.read()
print(content)
exec(content)
print()

file=open("practice2.py",'a')
file.write("#added a new line")
file.close()

file=open("practice2.py",'r')
content=file.read()
print(content)
exec(content)