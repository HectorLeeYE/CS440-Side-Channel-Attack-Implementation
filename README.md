# Implementation for CS440 Project Side Channel Timing Attack

Created on: 26 August 2025

Ideas:
1. Password Comparison Attack
2. Hashing Side Channel
3. Web Timing Attack on Different Endpoints

## Changelog
080925: Idea 3 is done -> server.py is in vulnerable_timingattack, and execute c4.py to detonate
Note that vulnerable_soundCPU can only be simulated, but the rainbow + lascar repo makes it seem possible 
180925: Added a frontend for vulnerable_timingAttack -> Think run ahead with vuln_timingAttack due to lack of time, and also ease of setting up to make it interactive since I can deploy it

## Implementation instructions for POC
1. Create a python virtual environment - Unless you don't mind messing up your local filesystem with varying package versions. Plus I installed a bunch of random packages to make things work, especially with the frontend display since i especially suck at (and also dont understand) react/jsx, and didnt clean up
2. Check it's using your virtual env python with `which python` and it should point to the virtual environment bin/python
2. `pip3 install -r requirements.txt` -> Please dont pipx, that's a system wide installation
4. `cd frontend && npm install & npm run dev` 
5. Get Docker, and build with
`docker compose up -d --build`.
Do it from the dir with compose.yml
6. Teardown with
`docker compose down`



## News Articles/Resources
[Lucky 13 TLS CBC Attack](https://en.wikipedia.org/wiki/Lucky_Thirteen_attack)
https://github.com/phonchi/awesome-side-channel-attack

[Possible Implementation of weak JWT](https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMROBBERT229JWT-50051)


