import asymmetric_encryption_decryption as asym

def encrypt_file(input_file, output_file):
    """
    Simply open the file, read the bytes, encrypt the data and write them out to a new file.
    """
    private_key, public_key = asym.get_keys()
    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the input file
    encrypted = asym.encryption(data, public_key)
    with open(output_file, 'wb') as f:
        f.write(encrypted)  # Write the encrypted bytes to the output file
    
    return private_key, public_key

def decrypt_file(private_key, input_file, output_file):
    """
    """
    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file
    decrypted = asym.decryption(data, private_key)
    with open(output_file, 'wb') as f:
        f.write(decrypted)  # Write the decrypted bytes to the output file

if __name__ == "__main__":
    input_file = 'file_to_encrypt_async.txt'
    out_file_encr = 'asym_encrypted_file.encrypted'
    out_file_decr = 'asym_decrypted_file.txt'
    private_key, public_key = encrypt_file(input_file, out_file_encr)
    decrypt_file(private_key, out_file_encr, out_file_decr)