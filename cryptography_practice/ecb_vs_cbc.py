from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

plaintext = b"ABCDEFGHIJKLMNOPABCDEFGHIJKLMNOP"
key = b"ThisIsA16ByteKey"

# ECB mode
ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_ciphertext = ecb_cipher.encrypt(pad(plaintext, AES.block_size))

print("ECB Ciphertext:", ecb_ciphertext.hex())

# CBC mode
iv = get_random_bytes(16)
cbc_cipher = AES.new(key, AES.MODE_CBC, iv)
cbc_ciphertext = cbc_cipher.encrypt(pad(plaintext, AES.block_size))

print("CBC Ciphertext:", cbc_ciphertext.hex())