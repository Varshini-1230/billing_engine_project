def password_strength(password):
    score=0
    reasons=[]
    if len(password)>8:
        score+=1
    else:
        reasons.append("Length must be greater than 8")
    has_digit=False
    for ch in password:
        if ch.isdigit():
            score+=1
            has_digit=True
            break
    else:
        reasons.append("Password must contain digit")
        
    has_upper=False
    for ch in password:
        if ch.isupper():
            score+=1
            has_upper=True
            break
    else:
        reasons.append("Password must contain atleast one uppercase letter")
        
    special_character="!@#$%^&*()_"
    for ch in password:
        if ch in special_character:
            score+=1
            break
    else:
        reasons.append("Password must contain Secial characters")
        
    repeated=False
    for length in range(1, len(password)//2+1):
        for i in range(len(password)-2*length+1):
            first = password[i:i+length]
            second = password[i+length:i+2*length]
            if first == second:
                repeated = True
                break
        if repeated:
            break
    if repeated:
        reasons.append("Password must not contain repeated sequences")
    else:
        score += 1
    
    found=False
    file=open("common.txt")
    for line in file:
        common=line.strip()
        
        if common.lower()==password.lower():
            found=True
            break
    if found:
        print("Password is too common")
        return False
    else:
        print("Password is not in the common list")
            
    if len(reasons)==0:
        print("Strong Password")
    else:
        print(score)
        print("Reasons for failure")
        print(f"{reasons}")
password=input("Enter the password:")
password_strength(password)
        