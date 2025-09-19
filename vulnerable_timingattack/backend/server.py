from flask import Flask, request, redirect, render_template, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
topsecretpassword = "PLSGIVEUSAPLUS"

@app.route("/timingAttack", methods=['POST'])
def testing_timingAttack():
    """
    Naive implementation of password checking (Could be under the hood)
    """
    # First, grab details from login.html
    if request.method == "POST":
        grabbed_request = request.get_json()
        entered_password = grabbed_request.get("password")

        # Next, compare with stored password to return false
        for i in range(min(len(entered_password), len(topsecretpassword))):
            if entered_password[i] != topsecretpassword[i]:
                # Wrong Password returned immediately since a char doesnt match
                time.sleep(0.01)                                #NOTE: THIS IS A MASSIVE CHEAT AS ITS ARTIFICIAL!     
                #return redirect(url_for("failure"))
                return jsonify({
                    "Message":"Password Wrong"
                }), 401

        if len(entered_password) != len(topsecretpassword):
            return jsonify({
               "Message":"Password Wrong"
            }), 401
        else:
            # Reached the end, so its correct password
            return jsonify({
                "Message":"Correct"
            }), 200

if __name__=="__main__":
    print('Current Password: ', topsecretpassword)
    app.run(host="0.0.0.0", port=5000, debug=True)