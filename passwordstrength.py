password = input("Enter a password: ")

cheaks = {
    "lenght ": len(password) >=9,
    "upper case": any(c.isupper() for c in password),
    "lower case": any(c.islower() for c in password),
    "digit": any(c.isdigit()for c in password),
    "special char": any(not c.isalnum() for c in password)
}

score = 0
for cheak in cheaks.values():
    if cheak:
        score +=1
print(f"Password Strength: {score}/5")

if score == 5:
    print("STRONG PASSWORD")
elif score >= 3:
    print("MEDIUM PASSWORD")
else:
    print("WEAK PASSWORD")

print("----END OF THE CODE----")

