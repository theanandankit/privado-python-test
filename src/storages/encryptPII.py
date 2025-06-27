from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

firstName = "123-45-6789" 

key = AESGCM.generate_key(bit_length=256)

aesgcm = AESGCM(key)

nonce = os.urandom(12)

ciphertext = aesgcm.encrypt(nonce, firstName.encode(), associated_data=None)
print("Encrypted PII:", ciphertext.hex())