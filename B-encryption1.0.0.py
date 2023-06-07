#     Welcome to B-encryption script !

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_AES(message, key):
    backend = default_backend()
    
    iv = os.urandom(16)
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message) + padder.finalize()
    
    cipher_text = encryptor.update(padded_data) + encryptor.finalize()
    
    return iv + cipher_text

# Demander à l'utilisateur d'entrer le message
message = input("Entrez votre message : ")

# Demander à l'utilisateur d'entrer la clé de chiffrement
key = input("Entrez la clé de chiffrement 256bits (32 caractères) : ")

# Convertir le message et la clé en bytes
message_bytes = message.encode()
key_bytes = key.encode()

# Vérifier la longueur de la clé
if len(key_bytes) != 32:
    raise ValueError("La clé doit être de 256 bits (32 octets)")

encrypted_message = encrypt_AES(message_bytes, key_bytes)
print("Message chiffré :", encrypted_message)
