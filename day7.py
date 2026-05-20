score = 0
#Q1 
ans = input("Q1. HTTP er Full Form ki").lower()
if ans == "hypertext transfer protocall":
    print("CORRECT, DARUN")
    score += 1
else :
    print(f"Worng! Answer : {ans}")
#Q2

ans = input ("Q2. HTTPS e S MANE KI BOJHAI ?").lower()
if ans == "s mane secure":
    print("CORRECT ! , Chaliye Ja")
    score += 1
else:
    print(f"Wrong ! Answer {ans}")

#Q3.
ans = input ("Q3. Full Form of IP Adress ?").lower()
if ans == "internet protocall adress":
    print("CORRECT ! , Chaliye Ja")
    score += 1
else :
    print(f"Wrong ! Answer {ans}")

#Q4. 
ans = input ("Q3. OSI Model e Kota Layer Ache?").lower()
if ans == "7":
    print("CORRECT ! , Excelent")
    score += 1
#Q5.
ans = input ("Q5. Firewall ki kaje lage ?").lower()
if ans == "network protect kore" or "network security dey" or "protect kore" or "security" or " protect":
    print("CORRECT ! , Almost Champion")
    score += 1
else: 
    print(f"Wrong ! Answer {ans}")

print(f"\n--- RESULT---")    
print(f"\n Tomar Score: {score}/5")
if score == 5:
    print("Outstanding ! Tui champion! 🏆")
elif score >= 3:
    print("Nice Try :Keep it up 🏆")
else:
    print("Need more Practice! Good")