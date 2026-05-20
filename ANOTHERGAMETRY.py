secret = ("HP")
guess = 0
chance = 5

while chance > 0:
    guess = str (input(f"Bol to Ami Ki Comapany Laptop Niyechi {chance} "))
    if guess == secret:
        print("WOW EKDOM THIK")
        break
    elif guess != secret:
        print ("TRY AGAIN , Hoyni ")
    chance = chance -1

if guess != secret:
 print(f"GAME OVER , Secret chilo {secret}" )
