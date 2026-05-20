secret = 50
guess = 0
chance = 5

while chance > 0 :
    guess = int (input(f"Guess kor ({ chance } chance baki ache :) "))
    if guess == secret:
       print("PERFECT, EKDOM THIK BOLCEHIS ")
       break

    elif guess > secret:
        print ("Try Again, Number Boro Hoyeche")
    else:
      print("Choto Hoyeche ,Chol Abar Chesta Kor")
    chance = chance - 1
 
if guess != secret:
   print (f"GAME OVER! Secret chilo {secret}")