from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt_file(input_file, output_file, key):
    # Generate a new IV for this file's encryption
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Open the original file in binary read mode and read its contents
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    # Pad and encrypt the file contents
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    # Save the IV followed by the ciphertext in the encrypted file
    with open(output_file, 'wb') as file:
        file.write(iv + ciphertext)


def decrypt_file(input_file, output_file, key):
    # Open the encrypted file and read the IV stored at the beginning
    with open(input_file, 'rb') as file:
        iv = file.read(16)
        ciphertext = file.read()

    # Recreate the cipher using the same key and IV
    decipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data and remove the padding
    plaintext = unpad(
        decipher.decrypt(ciphertext), AES.block_size
    )

    # Save the recovered contents to a new text file
    with open(output_file, 'wb') as file:
        file.write(plaintext)


# Generate one key to use for both encryption and decryption
key = get_random_bytes(16)

# Encrypt the original file
encrypt_file('cryptography_practice/message.txt', 'cryptography_practice/encrypted.bin', key) 
# Decrypt the encrypted file into a separate file 
decrypt_file('cryptography_practice/encrypted.bin', 'cryptography_practice/decrypted.txt', key)

print("File encrypted successfully.")
print("File decrypted successfully.")