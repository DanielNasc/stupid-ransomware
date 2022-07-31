import os
from cryptography.fernet import Fernet

# get all files in current dir ====

files = []

for file in os.listdir():
    if file in [ "decrypt.py", "ransomware.py", "key.key" ]:
        continue
    if os.path.isfile(file):
        files.append(file)

print("Arquivos encontrados:", files)

# key =============================

key = open("key.key", "rb").read()

# decrypt files====================

for file in files:
    print("Decriptando", file) 
    with open(file, "rb") as file_to_decrypt:
        contents = file_to_decrypt.read()
    decrypted_contents = Fernet(key).decrypt(contents)
    with open(file, "wb") as file_to_decrypt:
        file_to_decrypt.write(decrypted_contents)

