# Asymmetric encryption uses two keys - a private key and a public key. Public keys are given out for anyone to use,
# you make them public information. Anyone can encrypt data with your public key and then only those with the private key
# can decrypt the message. This also works the other way around but it is a convention to keep your private key secret.
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def get_keys():
    """
    To generate the two keys, we can call rsa.generate_private_key with some general parameters.
    The public key will be found in the object that holds the creation of the private key.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def store_private_key(private_key):
    """
    To store the keys in a file, they first need to be serialized and then written to a file. To store the private key, we need to use the following.
    """
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('private_key.pem', 'wb') as f:
        f.write(pem)

def store_public_key(public_key):
    """
    """
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('public_key.pem', 'wb') as f:
        f.write(pem)

def read_private_key():
    """
    The variable private_key will now have the private key.
    """
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
        return private_key

def read_public_key():
    """
    """
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
        return public_key

def encryption(message, public_key):
    """
    Encrypt the given message using the given public_key.
    """
    message = message.encode()
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

def decryption(encrypted, private_key):
    """
    decrypt the given encrypted message using the private_key.
    """
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message

if __name__ == "__main__":
    private_key, public_key = get_keys()
    store_private_key(private_key)
    store_public_key(public_key)
    private_key = read_private_key()
    public_key = read_public_key()
    message = 'encrypt me!'
    encrypted = encryption(message, public_key)
    print(f'Encrypted message: {encrypted}')
    original_message = decryption(encrypted, private_key)
    original_message = original_message.decode()
    print(f'Original message: {original_message}')
    assert message == original_message