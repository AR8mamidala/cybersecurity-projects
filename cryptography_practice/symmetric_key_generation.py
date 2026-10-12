# imports a function that generates random bytes for our key
from Crypto.Random import get_random_bytes
# gives us tools for converting binary data into hexadecimal
import binascii
# gives us tools for converting binary data into Base64
import base64

# generates 16 random bytes and stores it as the variable 'key'
key = get_random_bytes(16)
# .decode() converts the result from bytes into a normal Python string so it displays neatly
print("Hexadecimal:", binascii.hexlify(key).decode())
print("Base64:", base64.b64encode(key).decode())
