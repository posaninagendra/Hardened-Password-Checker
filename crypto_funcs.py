from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES

# Encryption of message using block cipher with the key = hpwd
def encrypt(hpwd, msg):
    key = str(long_to_bytes(hpwd))
    key = key.rjust(32, '0')
    iv = str(long_to_bytes(0, 16))
    encryption_suite = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = encryption_suite.encrypt(msg)
    return cipher_text

# Decryption of message using block cipher with the key = hpwd

def decrypt(hpwd):
    f = open("history.txt", 'r')
    cipher_text = f.read()
    f.close()
    key = str(long_to_bytes(hpwd))
    key = key.rjust(32, '0')
    iv = str(long_to_bytes(0, 16))
    decryption_suite = AES.new(key, AES.MODE_CBC, iv)
    return decryption_suite.decrypt(cipher_text)