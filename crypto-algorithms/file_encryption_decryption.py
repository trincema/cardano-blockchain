import symmetric_encryption_decryption as sym

def encrypt_file(input_file, output_file):
    """
    Simply open the file, read the bytes, encrypt the data and write them out to a new file.
    """
    key = sym.generate_random_key()
    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the input file
    encrypted = sym.encryption(key, data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)  # Write the encrypted bytes to the output file
    
    return key

def decrypt_file(key, input_file, output_file):
    """
    """
    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file
    decrypted = sym.decryption(key, data)
    with open(output_file, 'wb') as f:
        f.write(decrypted)  # Write the decrypted bytes to the output file

if __name__ == "__main__":
    input_file = 'file_to_encrypt.txt'
    out_file_encr = 'encrypted_file.encrypted'
    out_file_decr = 'decrypted_file.txt'
    key = encrypt_file(input_file, out_file_encr)
    decrypt_file(key, out_file_encr, out_file_decr)