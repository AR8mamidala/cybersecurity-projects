from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a random 128-bit key
key = get_random_bytes(16)

# Original message
plaintext = b"Hello, AES GCM!"

# Encrypt using AES-GCM
cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Store the nonce for decryption
nonce = cipher.nonce

print("Ciphertext:", ciphertext.hex())
print("Nonce:", nonce.hex())
print("Authentication Tag:", tag.hex())

# Decrypt and verify the message
decipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

try:
    # decrypt_and_verify() decrypts the ciphertext and checks the authentication tag
    decrypted = decipher.decrypt_and_verify(ciphertext, tag)
    print("Decrypted:", decrypted.decode())
    print("Authentication successful")
# If verification fails, it raises a ValueError.
except ValueError:
    print("Authentication failed")