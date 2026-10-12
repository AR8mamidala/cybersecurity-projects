from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# The b before the quotation marks tells Python to treat the text as bytes
key = b'ThisIsA16ByteKey'
# Create an AES cipher object using the key and ECB mode.
cipher = AES.new(key, AES.MODE_ECB)
plaintext = b"Hello, AES ECB!"
# Padding
padded_plaintext = pad(plaintext, AES.block_size)
# Encrypting the padded text
ciphertext = cipher.encrypt(padded_plaintext)
# The encrypted message is printed as a hexadecimal string
print("Ciphertext:", ciphertext.hex())

decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decrypted:", decrypted.decode())
