numbers=[10,25,30,45,50,75,90,100]
new_list=[]
for ele in numbers:
    if ele > 30 and ele % 5==0 and ele != 75:
        new_list.append(ele)
print(new_list)