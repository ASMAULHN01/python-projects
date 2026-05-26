from datetime import datetime

def log_login(username , status):
    file = open("login_log.txt", "a")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{time} - {username} - {status} \n")
    file.close()

log_login("Asmaul", "Sucess")
log_login("Hacker123", "Failed")
log_login("Jubair", "Sucess")
log_login("Fahad" , "Sucess")
log_login("Unknown" , "Failed")

chance = 3
while chance > 0:
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    if username == "Asmaul" and password == "password123":
        print("Login Sucessful !")
        log_login(username, "Sucess")
        break
    elif username == "Jubair" and password == "jubair456":
        print("Login sucessful !")
        log_login(username, "Sucess")
        break
    else:
        log_login(username, "Failed")
        chance -= 1
        if chance == 0:
            print("⚠️ ALERT: Suspicious activity detected! Account locked.")
        else:
            print(f"Login Failed! Try Again. {chance} chances left.")


print("Log file succesfully updated !")

#log reading 

file = open("login_log.txt", "r")
content = (file.read())
file.close()

print(content)