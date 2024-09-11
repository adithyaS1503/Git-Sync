import os
from cryptography.fernet import Fernet

# Load the encryption key from a file
def load_key():
    return open('secret.key', 'rb').read()

# Encrypt a single file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    # Read the file data
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the data
    encrypted_data = fernet.encrypt(file_data)

    # Write the encrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

    print(f"{file_path} has been encrypted.")

# Encrypt all files in a given directory (recursively)
def encrypt_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path)

# Main function to run the encryption for a given directory
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python encrypt_files.py <directory>")
    else:
        directory = sys.argv[1]
        if os.path.exists(directory):
            encrypt_files_in_directory(directory)
        else:
            print(f"Directory '{directory}' does not exist.")
