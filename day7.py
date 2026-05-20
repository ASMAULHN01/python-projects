score = 0
#Q1 
ans = input("Q1. What is Full Form of HTTP? ").lower()
if ans == "hypertext transfer protocall":
    print("CORRECT, Good")
    score += 1
else :
    print("Worng! Answer : hypertext transfer protocall")
#Q2

ans = input ("Q2. WHAT S means at HTTPS ?").lower()
if ans == "s for secure":
    print("CORRECT ! , Keep it up")
    score += 1
else:
    print("Wrong ! Answer : s for secure")

#Q3.
ans = input ("Q3. Full Form of IP Adress ?").lower()
if ans == "internet protocall adress":
    print("CORRECT ! , Chaliye Ja")
    score += 1
else :
    print("Wrong ! Answer :internet protocall adress ")

#Q4. 
ans = input ("Q4. How many layes's at OSI Model?").lower()
if ans == "7":
    print("CORRECT ! , Excelent")
    score += 1
else :
    print("Wrong ! Answer : 7")

#Q5.
ans = input ("Q5. what is the function of Firewall ?").lower()
if ans == "network protecting " or "network security" or "protecting internet" or "security" or " protect":
    print("CORRECT ! , Almost Champion")
    score += 1
else: 
    print("Wrong ! Answer: network protecting or network security or protecting internet or security or  protect")


print(f"\n--- RESULT---")    
print(f"\n Your Score: {score}/5")
if score == 5:
    print("Outstanding ! You are a champion! 🏆")
elif score >= 3:
    print("Nice Try :Keep it up 🏆")
else:
    print("Need more Practice! Good")