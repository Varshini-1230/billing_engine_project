n=int(input("Enter n value: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(n):
        print("*",end="")
    print()



#another approch 
num=int(input("Enter n value:"))
for i in range(n,0,-1):
    print(i*" " + "*" * num)