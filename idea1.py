from flask import Flask, request
import time

app = Flask(__name__)
secret_password = "supersecret"

@app.route("/login", methods=["POST"])
def login():
    user_input = request.form.get("password", "")
    for i in range(min(len(user_input), len(secret_password))):
        
        if user_input[i] != secret_password[i]:
            return "Invalid", 403        
        time.sleep(0.05)            # Simulate latency with backend 
                                    ## Hash password -> Compare password with hashed input stored at the backend and possibly also salt the hash

    if user_input == secret_password:
        return "Welcome!"

    return "Invalid", 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)