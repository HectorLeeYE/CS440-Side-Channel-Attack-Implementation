# Timing Attack
[Python Version 3.2 is vulnerable](https://www.wiz.io/vulnerability-database/cve/cve-2020-25659)
[CVE-2020-25659](https://vulert.com/vuln-db/pypi-cryptography-14696)


This is the implementation of said version


# Update Log
310825: Implemented naive version of PKCS1v15 which is apparently vulnerable to timing attacks, **consider implementing fakelag with sleep(10) into app.py to exaggerate timing requests!
070925: Don't use it - I can't get it to work for some reason. 
There's already an existing version that uses == to compare which isnt a constant operation so it is ok for a timing attack 

070925: Implementing a new version- check out the other folder 



## Stuff installed
pip install cryptography==3.2
pip install requests