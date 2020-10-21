BLOCK_SIZE = 16
#key = b"1234567890123456" # TODO change to something with more entropy
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
    print(data)
    return data[:-data[-1]]

def encrypt(message, key):
    IV = Random.new().read(BLOCK_SIZE)
    print(type(IV))
    print(type(key))
    aes = AES.new(key, AES.MODE_CBC, IV)
    return base64.b64encode(IV + aes.encrypt(pad(message)))

def decrypt(encrypted, key):
    encrypted = base64.b64decode(encrypted)
    print(base64.b64encode(encrypted))
    IV = encrypted[:BLOCK_SIZE]
    print(base64.b64encode(IV))
    print(type(IV))
    print(type(encrypted))
    print(type(key))
    aes = AES.new(key, AES.MODE_CBC, IV)
    print(base64.b64encode(encrypted[BLOCK_SIZE:]))
    return unpad(aes.decrypt(encrypted[BLOCK_SIZE:]))


message = "hP2V3xrvCMjXd8SSICqB2230eoEuaUzBoXeoWx20khak94xJXYjTr5+yAPkqvvSb00xeBlTatNJkCMpVgyuuvnFKFHxczsSHN7vbdKPIN/QWKfARKC6x+LqqUYyj/ECtUL30UjbZEDzi/GmRGa6fu42NtoPcqUWbxJkr+V5j/zRadHotIR/CjPAU4vqtXomy"
h = hashlib.md5('asd'.encode())
#b = (h.hexdigest()).encode()
#x = binascii.hexlify(b)
#y = str(x,'ascii')
b = h.hexdigest()
b = str.encode(b)
print(b)

print(decrypt(message,b))

tobeencrypted = "[{\"servicename\":\"asd\",\"username\":\"asd\",\"password\":\"asd\"},{\"servicename\":\"asdef\",\"username\":\"asdef\",\"password\":\"asdef\"}]"
encrypteddata=encrypt(tobeencrypted.encode(),b)
print(encrypteddata)
#binrep = binascii.hexlify(encrypteddata)
#y = str (binrep,'ascii')
#print(y)
#as_int = int(h.hexdigest(), 10)
#print(as_int)


# JS decryption tested https://jsfiddle.net/cskj7phL/