file=open("paragraph.txt",'w')
file.write("Python is a simple and popular programming language. It is easy to learn and is used to create websites, applications, automation programs, and data analysis projects. Python has simple syntax, which makes it suitable for beginners. Many companies use Python for different types of software development.")
file.close()

file=open("paragraph.txt",'r')
words=file.read().split(" ")
print("The count of number of words:",len(words))
