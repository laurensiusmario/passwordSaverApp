BLOCK_SIZE = 16
from Crypto.Cipher import AES
import base64
from Crypto.Hash import MD5
import hashlib
import binascii
from Crypto import Random

def pad(data):
    length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + (chr(length)).encode()*length

def unpad(data):
    return data[:-data[-1]]

def encrypt(message, key):
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(key, AES.MODE_CBC, IV)
    return base64.b64encode(IV + aes.encrypt(pad(message)))

def decrypt(encrypted, key):
    encrypted = base64.b64decode(encrypted)
    IV = encrypted[:BLOCK_SIZE]
    aes = AES.new(key, AES.MODE_CBC, IV)
    return unpad(aes.decrypt(encrypted[BLOCK_SIZE:]))

def processDecryptKey(key):
    h = hashlib.md5(key.encode())
    b = h.hexdigest()
    b = str.encode(b)
    return b