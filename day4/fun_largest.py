def largest_num(list):
    largest=list[0]
    for ele in list:
        if ele >largest:
            largest=ele
    return largest
list=[9,8,3,20]
print(largest_num(list))