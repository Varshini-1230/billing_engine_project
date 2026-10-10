l1=[10, 20, 10, 30, 20, 40, 30]
#print(set(l1))

dupli=[]
for ele in l1:
    if ele not in dupli:
        dupli.append(ele)
print("Removed duplicates:",dupli)