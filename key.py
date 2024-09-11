from cryptography.fernet import Fernet

# Generate and print the key
key = Fernet.generate_key()
print(f"Your key: {key.decode()}")

# Save the key to a file (you can reuse this on both machines)
with open('secret.key', 'wb') as key_file:
    key_file.write(key)
