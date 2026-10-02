import hashlib
import json

file_check = input("What file would you like to check? ")

try:
    # The file is opened and read
    with open(file_check, "r") as file:
        # .read() gets the file contents, .encode() converts text to bytes and hashlib.sha256() creates a SHA-256 hash
        file_hash = hashlib.sha256(file.read().encode())
except FileNotFoundError:
    print("This file does not exist.")
    exit()

try:
    with open("hashes.json", "r") as file:
        hashes = json.load(file)
        if file_check in hashes:
            # The hash is saved as the saved_hash variable
            saved_hash = hashes[file_check]
        else:
            file_add = input("This file has no stored hash. Would you like to add it (Y/N)? ")
            if file_add.upper() == "Y":
                hashes[file_check] = ""
except FileNotFoundError:
    hashes = {}
    file_add = input("There are no hashes stored yet. Do you want to add the file (Y/N)? ")
    if file_add.upper() == "Y":
        hashes[file_check] = ""

# hexdigest() is a method for converting the hash into a long hexadecimal string
print(f"This is the hash for this file: {file_hash.hexdigest()}")

def save_hashes():
    # This opens the hashes.json file
    with open("hashes.json" , "w") as file:
        # The updated hashes dictionary is saved to the JSON file
        hashes[file_check] = file_hash.hexdigest()
        json.dump(hashes, file, indent=4)

if file_check in hashes:
    if hashes[file_check] == "":
        print("This is a new file. A previous hash is not stored.")
        save_hashes()
    elif file_hash.hexdigest() == saved_hash:
        print("The hashes match. The file has not been changed or corrupted.")
    else:
        print("The hashes do not match- this file may have been corrupted!")
else:
    print("You have not added this file.")