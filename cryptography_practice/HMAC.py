import hmac
import hashlib

# Generate an HMAC using SHA-256
def generate_hmac(key, message):
    hmac_value = hmac.new(key, message, hashlib.sha256).hexdigest()
    return hmac_value


# Verify an HMAC by recalculating it
def verify_hmac(key, message, given_hmac):
    # Generate a new HMAC using the same key and message
    computed_hmac = generate_hmac(key, message)

    # Compare both HMACs securely
    return hmac.compare_digest(computed_hmac, given_hmac)


# Ask the user for a secret key and message
key = input("Enter secret key: ").encode()
message = input("Enter message: ").encode()

# Generate and display the HMAC
hmac_value = generate_hmac(key, message)
print("Generated HMAC:", hmac_value)

# Ask the user to enter an HMAC for verification
user_hmac = input("Enter HMAC to verify: ")

# Check whether the HMAC is valid
if verify_hmac(key, message, user_hmac):
    print("HMAC verified successfully.")
else:
    print("HMAC verification failed.")