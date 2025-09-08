# Timing Attack
[Python Version 3.2 is vulnerable](https://www.wiz.io/vulnerability-database/cve/cve-2020-25659)
[CVE-2020-25659](https://vulert.com/vuln-db/pypi-cryptography-14696)



# Update Log
310825: Implemented naive version of PKCS1v15 which is apparently vulnerable to timing attacks, **consider implementing fakelag with sleep(10) into app.py to exaggerate timing requests!
070925: Don't use it - I can't get it to work for some reason. 
There's already an existing version that uses == to compare which isnt a constant operation so it is ok for a timing attack 

TODO: Maybe try the vuln cve cryptography version another day 
Currently, server.py is the flask server
the bomb is in bombkit/c4.py so just run that

Edit the TOPSECRETPASSWORD variable in server.py, and extend the wordlist as well to accomdate for your changed top secret password