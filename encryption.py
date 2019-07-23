from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
import binascii
import hashlib


master_password = "EAwpaeBxscpvSNkYQFc7Laq2"

key = hashlib.sha256(master_password.encode('utf-8')).digest()



def encrypt(key, file):
    with open(file, 'rb') as myfile:
        plaintext = myfile.read()
    iv = Random.new().read(AES.block_size)
    iv_int = int(binascii.hexlify(iv), 16)
    ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    ciphertext = aes.encrypt(plaintext)
    with open(file, "wb") as afile:
        afile.write(ciphertext)
        afile.truncate()
    with open("ivfile", "wb") as ifile:
        ifile.write(iv)
    #return (iv, ciphertext)


def decrypt(key, ivfile, file):
    with open(file, 'rb') as myfile:
        ciphertext = myfile.read()
    with open(ivfile, "rb") as ifile:
        iv = ifile.read()
    iv_int = int(binascii.hexlify(iv), 16)
    ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    plaintext = aes.decrypt(ciphertext)
    # with open(file, "wb") as afile:
    #     afile.write(plaintext)
    #     afile.truncate()
    # plaintext = str(plaintext)
    return plaintext


#encrypt(key, "new.json")
#decrypt(key, "ivfile", "new.json")
