sen=input().lower()
words=sen.split()
smallest=words[0]
for word in words:
    if word<smallest:
        smallest=word
print(smallest)