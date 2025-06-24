from Crypto.Cipher import AES

key = b'your_16_or_32_byte_key_here'  # Must be 16 or 32 bytes for AES-128 or AES-256
iv = b'your_16_byte_iv_here'          # Must be 16 bytes for CBC mode

cipher = AES.new(key, AES.MODE_CBC, iv)