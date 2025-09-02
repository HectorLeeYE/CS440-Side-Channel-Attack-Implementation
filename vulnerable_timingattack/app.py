from flask import Flask, request, redirect, render_template, url_for
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

app = Flask(__name__)
topsecretpassword = "SUPERDUPERTOPSECRETPASSWORD"       #Global variable for password- No time to implement putting variables inside requests and dealing with .html frontend


def encrypt_and_store():
    '''
    1. Encrypts topsecretpassword with pub
    2. Store topsecretpassword in memory 
    3. Sets up pri
    '''
    global ciphertext                   # Global variable -> No time to implement proper var passing again
    global public_key                   # Global variable -> No time + save rss since pointless to reopen file
    global private_key

    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

        
    ciphertext = public_key.encrypt(
        topsecretpassword.encode(),     # Encode since encryption takes bytes, not str()
        padding.PKCS1v15()              # The weak and also vulnerable cryptography version 
    )

    #print("CipherText: ", ciphertext)

    assert ciphertext is not None, "Ciphertext encryption failed, not found in memory"

    return 'Encrypt and Store DONE'
    


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
        

        # Next, compare with stored password to return false
        for i in range(len(topsecretpassword)):
            if entered_password[i] != topsecretpassword[i]:
                # Wrong Password returned immediately since a char doesnt match
                return redirect(url_for("failure"))

        # Reached the end, so its correct password
        return redirect(url_for("success"))

    return render_template("timingAttackFrontend.html")


@app.route("/login", methods=['POST'])
def padding_oracle():
    """
    Demonstrates RSA PKCS#1 v1.5 padding oracle.
    - If the ciphertext has valid PKCS#1 v1.5 padding, decryption succeeds
    - If the padding is invalid, cryptography raises an exception
    """

    # Client sends ciphertext instead of plaintext password
    if request.method == "POST":
        ciphertext_from_client = request.form['ciphertext'].encode("latin1")

    try:
        # Try to decrypt the ciphertext
        decrypted = private_key.decrypt(
            ciphertext_from_client,
            padding.PKCS1v15()   # vulnerable padding
        )
        # If decryption succeeds, return positive response
        return "<p>Valid Padding: Ciphertext Decrypted</p>"

    except ValueError:
        # Cryptography raises ValueError if padding is invalid
        return "<p>Invalid Padding!</p>"

    except Exception:
        # Catch other errors separately (rare but good practice)
        return "<p>General Error!</p>"


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/failure")
def failure():
    return render_template("failure.html")


if __name__=="__main__":
    encrypt_and_store()
    app.run(debug=True)