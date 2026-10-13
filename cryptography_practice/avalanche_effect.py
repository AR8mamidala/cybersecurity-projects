import hashlib

# Ask the user to enter the original message
message1 = input("Enter the original message: ")

# Ask the user to enter a slightly modified message
message2 = input("Enter the modified message: ")

# Convert both messages into bytes
message1_bytes = message1.encode()
message2_bytes = message2.encode()

# Generate an MD5 hash for each message
hash1 = hashlib.md5(message1_bytes).hexdigest()
hash2 = hashlib.md5(message2_bytes).hexdigest()

# Display both hashes
print("Original MD5 hash:", hash1)
print("Modified MD5 hash:", hash2)

# Check whether the hashes are different
if hash1 != hash2:
    print("The hashes are different.")
else:
    print("The hashes are the same.")