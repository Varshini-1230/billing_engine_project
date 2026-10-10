str=input()
v_count=0
c_count=0
d_count=0
for char in str:
    if char in "0123456789":
        d_count+=1
    elif char in "aeiouAEIOU":
        v_count+=1
    else:
        c_count+=1
print("Vowels: ",v_count)
print("Consonants: ",c_count)
print("Digits: ",d_count)