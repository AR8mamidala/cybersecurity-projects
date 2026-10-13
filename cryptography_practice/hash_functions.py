import hashlib

# Ask the user to enter a message
message = input("Enter a message: ")

# Convert the message from a string into bytes
message_bytes = message.encode()

# Generate a SHA-256 hash object from the message
hash_object = hashlib.sha256(message_bytes)

# Convert the hash into a readable hexadecimal string
hash_value = hash_object.hexdigest()

# Display the generated hash
print("Generated SHA-256:", hash_value)

# Ask the user for a hash to compare against
expected_hash = input("Enter expected hash: ")

# Check whether the two hashes are identical
if hash_value == expected_hash:
    print("Hashes match.")
else:
    print("Hashes do not match.")