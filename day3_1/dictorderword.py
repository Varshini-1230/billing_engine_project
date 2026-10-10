sen=input("Enter sentence:")
words=sen.split(" ")
first=words[0]
for word in words:
    for i in range(min(len(word),len(first))):
        if ord(word[i].lower()) < ord(word[i+1].lower()):
            first=word
            break
        elif ord(word[i].lower()) < ord(word[i+1].lower()):
            break
print(first)
print()

    
#Another approch    
sen =input().lower()
words=sen.split(" ")
smallest=words[0]
for word in words:
    if word < smallest:
        smallest=word
print(smallest)