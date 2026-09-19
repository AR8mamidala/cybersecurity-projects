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

