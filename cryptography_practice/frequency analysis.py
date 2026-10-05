# Function to perform frequency analysis on a ciphertext
def frequency_analysis(ciphertext):
    frequency = {} # Dictionary to store letter counts
    for char in ciphertext:
        if char.isalpha(): # Ignore non-alphabetic characters
            char = char.lower() # Treat all letters as lowercase
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
 
    # Sort the dictionary by frequency (highest first)
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency

# Main program to interact with the user
print("\nWelcome to the Frequency Analysis Program!")
ciphertext = input("Enter the ciphertext: ")

# Perform frequency analysis
analysis_result = frequency_analysis(ciphertext)

# Display the results
print("\nFrequency Analysis Result:")
for letter, count in analysis_result:
    print(f"{letter}: {count}")