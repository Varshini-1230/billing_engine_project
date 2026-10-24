l1=list(map(int,input().split()))
s=set()
for ele in l1:
    if ele not in s:
        s.add(ele)
print(s)
