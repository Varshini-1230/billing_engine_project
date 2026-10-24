l1=list(map(int,input().split()))
smallest=l1[0]
largest=l1[0]
for ele in l1:
    if ele < smallest:
        smallest=ele
for ele in l1:
    if ele > largest:
        largest=ele
print('Smallest:',smallest)
print("largest:",largest)
