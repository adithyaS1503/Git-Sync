import os
from cryptography.fernet import Fernet

# Load the encryption key from a file
def load_key():
    return open('secret.key', 'rb').read()

# Decrypt a single file
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    # Read the encrypted data
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)

    # Write the decrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"{file_path} has been decrypted.")

# Decrypt all files in a given directory (recursively)
def decrypt_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path)

# Main function to run the decryption for a given directory
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python decrypt_files.py <directory>")
    else:
        directory = sys.argv[1]
        if os.path.exists(directory):
            decrypt_files_in_directory(directory)
        else:
            print(f"Directory '{directory}' does not exist.")
