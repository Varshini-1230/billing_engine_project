numbers=[12,5,8,21,4,15,10]
largest = numbers[0]
smallest=numbers[0]
sum=0
for ele in numbers:
    if ele > largest:
        largest=ele
for ele in numbers:
    if ele < smallest:
        smallest = ele
for ele in numbers:
    sum+=ele
print(largest)
print(smallest)
print(sum)