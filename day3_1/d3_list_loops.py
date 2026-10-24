list1=list(map(int, input().split()))
#list1=[4,15,8,21,3,17]
#print(list1)
list2=[]
for ele in list1:
    if ele > 10:
        list2.append(ele)
print(list2)