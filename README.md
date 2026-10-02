# cybersecurity-projects

This repository contains independent cybersecurity projects that I am developing to build practical skills in Python, cybersecurity, and security tools.

## Projects

### File Integrity Checker

A Python-based file integrity checker that uses SHA-256 hashing to detect whether files have been modified.

#### Features

- Generates SHA-256 hashes for files
- Stores baseline hashes in a JSON file
- Checks files against their stored hashes
- Detects when a file has been modified
- Supports checking multiple files
- Handles missing files and files without stored hashes

#### How It Works

The program reads the selected file and generates a SHA-256 hash from its contents. The hash is stored in `hashes.json` as a baseline for future checks.

When the same file is checked again, a new hash is generated and compared with the stored hash. If the hashes match, the file has not changed. If they differ, the program reports that the file may have been modified or corrupted.

#### Technologies Used

- Python
- `hashlib`
- `json`
- SHA-256

#### Testing

The project was tested by:

- Adding a new file and storing its baseline hash
- Checking an unchanged file
- Modifying a file and detecting the changed hash
- Rechecking a modified file to confirm the original baseline was preserved
- Checking a second file
- Checking a file that does not exist

---

### Security Log Analyser

A Python-based security log analyser that identifies suspicious failed login activity by analysing IP addresses and login times.

#### Features

- Reads a security log line by line
- Identifies failed login attempts
- Groups failed attempts by IP address
- Counts failed login attempts for each IP
- Allows the user to set a suspicious attempt threshold
- Calculates the time between consecutive login attempts
- Allows the user to set a rapid-login threshold
- Detects login activity that may indicate a brute-force attack

#### How It Works

The program reads `security.log` line by line and identifies entries containing failed login attempts. It extracts the IP address, date and time from each entry and stores this information in a dictionary.

The program then counts the failed attempts associated with each IP address and calculates the time differences between consecutive attempts. The user can set thresholds for both the number of failed attempts and the time between attempts. IP addresses exceeding these thresholds are reported as suspicious.

The current output displays the date and time of the most recent failed login recorded for each IP address.

#### Testing

The `security.log` file used for testing was AI-generated test data designed to contain different patterns of failed login activity.

The project was tested by:

- Counting the total number of failed login attempts
- Grouping failed attempts by IP address
- Testing different failed-attempt thresholds
- Testing different rapid-login thresholds
- Detecting an IP address with rapid consecutive attempts
- Confirming that IP addresses below the configured threshold were not flagged
- Testing the `None detected` output when no suspicious activity was found

#### Technologies Used

- Python
- `datetime`
- Dictionaries
- File handling
- String processing