str=input()
count=0
for ch in str:
    if ch in "aeiouAEIOU":
        count+=1
print("Number of vowels:",count)
