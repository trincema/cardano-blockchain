# Symmetric encryption is when a key is used to encrypt and decrypt a message, so whoever encrypted it can decrypt it.
# The only way to decrypt the message is to know what was used to encrypt it; kind of like a password.

import cryptography
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_random_key():
    """
    There are two main ways to get a key, we can either generate a new one or use one that has previously been generated.
    These keys need to be in a particular format so make sure to get this right.
    key will now have the value of a URL safe base64 encoded key.
    This key will have a type of bytes, so if you want a string you can call key.decode() to convert from UTF-8 to Pythons string type.
    """
    key = Fernet.generate_key()
    return key

def generate_key_from_password(password_provided):
    """
    The variable key will now have the value of a url safe base64 encoded key.
    """
    password = password_provided.encode()  # Convert to type bytes
    salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    return key

def encryption(key, message_provided):
    """
    To encrypt a message, you will need a key (as previously discussed) and your message as type bytes
    (you can convert strings to bytes using .encode()).
    The variable encrypted will now have the value of the message encrypted as type bytes. This is also a URL safe base64 encoded key.
    """
    message = message_provided.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)  # Encrypt the bytes. The returning object is of type bytes
    return encrypted

def decryption(key, encrypted_message):
    """
    To decrypt a message, you will need the same key and the encrypted message (still in bytes).
    The variable decrypted will now have the value of the original message (which was of type bytes).
    If a different key to the one used to encrypt is provided when decrypting, a cryptography.fernet.InvalidToken will be raised.
    Catching this error will allow you to tell if the incorrect key was provided;
    """
    try:
        f = Fernet(key)
        decrypted = f.decrypt(encrypted_message)  # Decrypt the bytes. The returning object is of type bytes
        return decrypted.decode()
    except InvalidToken as e:
        print("Invalid Key - Unsuccessfully decrypted")

def decode_key(key):
    return key.decode()

def store_key(key):
    """
    One way of keeping your keys safe is to keep them in a file.
    """
    file = open('key.key', 'wb')  # Open the file as wb to write bytes
    file.write(key)  # The key is type bytes still
    file.close()

def read_key():
    """
    If you have previously saved your key using the method I showed, you can read the key back out using the following code.
    The key will now be read into the variable key and will be type bytes.
    """
    file = open('key.key', 'rb')  # Open the file as wb to read bytes
    key = file.read()  # The key will be type bytes
    file.close()

if __name__ == "__main__":
    message = "my deep dark secret"
    key = generate_random_key()
    store_key(key)
    encrypted = encryption(key, message)
    decrypted = decryption(key, encrypted)
    print(f'Original message: {message}')
    print(f'Encrypted: {encrypted.decode()}')
    print(f'Decrypted: {decrypted}')
    assert message == decrypted  # The original message and decrypted message are the same