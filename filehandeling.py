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

print("Log file succesfully updated !")

#log reading 

file = open("login_log.txt", "r")
content = (file.read())
file.close()

print(content)