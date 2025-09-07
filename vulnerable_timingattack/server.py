from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)
topsecretpassword = "$UP3RS3CR3TP@$$W0RD!"       #Global variable for password- No time to implement putting variables inside requests and dealing with .html frontend


@app.route("/timingAttack", methods=['POST', 'GET'])
def testing_timingAttack():
    """
    Naive implementation of password checking (Could be under the hood)
    """

    # First, grab details from login.html
    if request.method == "POST":
        entered_password = request.form['password']

        # Fail due to diff length of password 
        if len(entered_password) != len(topsecretpassword):
            return redirect(url_for("failure"))
        
        else:
            # Next, compare with stored password to return false
            for i in range(len(topsecretpassword)):
                if entered_password[i] != topsecretpassword[i]:
                    # Wrong Password returned immediately since a char doesnt match
                    return redirect(url_for("failure"))

        # Reached the end, so its correct password
        return redirect(url_for("success"))

    return render_template("timingAttackFrontend.html")


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/failure")
def failure():
    return render_template("failure.html")


if __name__=="__main__":
    app.run(debug=True)