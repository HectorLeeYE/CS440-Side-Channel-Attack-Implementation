from flask import Flask, request, redirect, render_template, url_for
import time

app = Flask(__name__)
topsecretpassword = "BCDEA"       #Global variable for password- No time to implement putting variables inside requests and dealing with .html frontend
                                    ## The only special chars are ! @

@app.route("/timingAttack", methods=['POST', 'GET'])
def testing_timingAttack():
    """
    Naive implementation of password checking (Could be under the hood)
    """

    # First, grab details from login.html
    if request.method == "POST":
        entered_password = request.form['password']
        print('Current Password: ', entered_password)

        # Next, compare with stored password to return false
        for i in range(min(len(entered_password), len(topsecretpassword))):
            if entered_password[i] != topsecretpassword[i]:
                # Wrong Password returned immediately since a char doesnt match
                time.sleep(0.3)                                #NOTE: THIS IS A MASSIVE CHEAT AS ITS ARTIFICIAL!     
                #return redirect(url_for("failure"))
                return "failure"

        if len(entered_password) != len(topsecretpassword):
            return "failure"
            
        # Reached the end, so its correct password
        return "success"

    return render_template("timingAttackFrontend.html")


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/failure")
def failure():
    return render_template("failure.html")


if __name__=="__main__":
    print('Current Password: ', topsecretpassword)
    app.run(debug=True)