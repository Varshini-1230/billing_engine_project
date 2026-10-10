num=int(input("Enter a number:"))
count=0

while num>0:
    digit=num%10
    num=num//10
    if digit%2==0:
        count+=1
print(count)