from flask import Flask, request, redirect, render_template, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
topsecretpassword = "BCDEA"       #Global variable for password- No time to implement putting variables inside requests and dealing with .html frontend
                                    ## The only special chars are ! @

@app.route("/timingAttack", methods=['POST'])
def testing_timingAttack():
    """
    Naive implementation of password checking (Could be under the hood)
    """
    # First, grab details from login.html
    if request.method == "POST":
        print(request)
        entered_password = request.json['password'][0]
        print('Current Password: ', entered_password)

        # Next, compare with stored password to return false
        for i in range(min(len(entered_password), len(topsecretpassword))):
            if entered_password[i] != topsecretpassword[i]:
                # Wrong Password returned immediately since a char doesnt match
                time.sleep(0.3)                                #NOTE: THIS IS A MASSIVE CHEAT AS ITS ARTIFICIAL!     
                #return redirect(url_for("failure"))
                return jsonify({
                    "Message":"Password Wrong"
                }), 401

        if len(entered_password) != len(topsecretpassword):
            return jsonify({
               "Message":"Password Wrong"
            }), 401
            
        # Reached the end, so its correct password
        return jsonify({
            "Message":"Correct"
        }), 200

if __name__=="__main__":
    print('Current Password: ', topsecretpassword)
    app.run(debug=True)