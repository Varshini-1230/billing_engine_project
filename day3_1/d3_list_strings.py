words=["apple","banana","kiwi","orange","grape"]
new_list=[]
for word in words:
    if len(word)>5:
        new_list.append(word)
print(new_list)