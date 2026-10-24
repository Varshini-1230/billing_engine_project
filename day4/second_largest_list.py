l1=list(map(int,input().split()))
second=l1[0]
largest=l1[0]
for ele in l1:
    if ele >largest:
        second=largest
        largest=ele
    elif ele >second and ele != largest:
        second=ele
print("Second largest number:",second) 