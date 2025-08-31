# Timing Attack
[Python Version 3.2 is vulnerable](https://www.wiz.io/vulnerability-database/cve/cve-2020-25659)
[CVE-2020-25659](https://vulert.com/vuln-db/pypi-cryptography-14696)


This is the implementation of said version


# Update Log
310825: Implemented naive version of PKCS1v15 which is apparently vulnerable to timing attacks, **consider implementing fakelag with sleep(10) into app.py to exaggerate timing requests!

## Stuff installed
pip install cryptography==3.2
pip install requests