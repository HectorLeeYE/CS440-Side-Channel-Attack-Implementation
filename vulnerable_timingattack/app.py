from flask import Flask, request
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

app = Flask(__name__)
topsecretpassword = "Password1"       #Global variable for password- No time to implement putting variables inside requests and dealing with .html frontend


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

    print("CipherText: ", ciphertext)

    assert ciphertext is not None, "Ciphertext encryption failed, not found in memory"

    return 'Encrypt and Store DONE'
    


@app.route("/login", methods=['POST'])
def testing_timingAttack():

    # First, grab details from login.html
    if request.method == "POST":
        entered_password = request.form['password']
    

    try:
        # Next, decrypt the password
        decrypted = private_key.decrypt(
            ciphertext,
            padding.PKCS1v15()              # The weak and also vulnerable cryptography version 
    )

    except Exception:
        return "<p>Error While Decrypting!</p>"


    # Last, compare with stored password to return false
    if (decrypted.decode() == entered_password):


        # Correct Password
        return "<p>Successfully Entered </p>"

    else:
        
        # Wrong Password 
    


        return "<p>Wrong!</p>"


if __name__=="__main__":
    encrypt_and_store()
    app.run(debug=True)