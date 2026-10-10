str=input().replace('"',"").split(" ")
freq={}
for word in str:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)
