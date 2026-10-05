#Function to encrypt a message using Caesar Cipher
def caesar_cipher(text, shift):
    encrypted_text = "" # Start with an empty string
    for char in text:
        if char.isalpha(): # Check if the character is a letter
            if char.islower(): # For lowercase letters
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else: # For uppercase letters
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += new_char # Add the shifted character to the result
        else:
            encrypted_text += char # Leave non-alphabet characters unchanged
    return encrypted_text

print(caesar_cipher("hello world", 3)) 

# Function to decrypt a message using Caesar Cipher
def caesar_decrypt(text, shift):
    return caesar_cipher(text, -shift) # Use a negative shift to reverse encryption

# Main program to interact with the user
print("Welcome to the Caesar Cipher Program!")
message = input("Enter the message you want to encrypt: ")
shift_value = int(input("Enter the shift value (positive or negative): "))

# Encrypt the message
encrypted_message = caesar_cipher(message, shift_value)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = caesar_decrypt(encrypted_message, shift_value)
print("Decrypted Message:", decrypted_message)
