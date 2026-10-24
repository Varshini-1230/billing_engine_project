list1=list(map(int, input().split()))
#list1=[1,2,3,2,4,1,5]
freq=0
for i in range(len(list1)):
    if list1.count(list1[i])>1:
        if list1.index(list1[i])==i:
            freq+=1
print(freq)