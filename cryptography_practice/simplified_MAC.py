import hashlib

# Generate a MAC using a secret key and message
def generate_mac(key, message):
    data = key + message

    # Generate a SHA-256 hash of the combined data
    mac = hashlib.sha256(data).hexdigest()

    return mac


# Verify a MAC by generating it again and comparing
def verify_mac(key, message, given_mac):
    # Recalculate the MAC using the same key and message
    computed_mac = generate_mac(key, message)

    # Check whether the calculated MAC matches the given MAC
    return computed_mac == given_mac


# Ask the user for a secret key and message
key = input("Enter secret key: ").encode()
message = input("Enter message: ").encode()

# Generate and display the MAC
mac_value = generate_mac(key, message)
print("Generated MAC:", mac_value)

# Ask the user to enter a MAC for verification
user_mac = input("Enter MAC to verify: ")

# Check whether the MAC is valid
if verify_mac(key, message, user_mac):
    print("MAC verified successfully.")
else:
    print("MAC verification failed.")