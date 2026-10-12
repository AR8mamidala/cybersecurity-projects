from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
# Generate a random 16-byte initialisation vector (IV)
iv = get_random_bytes(16)
# Create an AES cipher using CBC mode and the IV
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = b"Learning AES CBC mode!"
padded_plaintext = pad(plaintext, AES.block_size)
ciphertext = cipher.encrypt(padded_plaintext)
print("Ciphertext:", ciphertext.hex())

decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decrypted:", decrypted.decode())