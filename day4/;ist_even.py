l1=list(map(int,input().split()))
l2=[]
for ele in l1:
    if ele%2==0:
        l2.append(ele)
print(l2)
