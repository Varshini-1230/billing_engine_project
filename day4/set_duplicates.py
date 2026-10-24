s1={4,6,5,3,4,5,6}
print(s1)
print(set(s1))

dup=[]
for ele in s1:
    if ele not in dup:
        dup.append(ele)
print(set(dup))
