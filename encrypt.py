import encryption
import hashlib

master_password = "EAwpaeBxscpvSNkYQFc7Laq2"

key = hashlib.sha256(master_password.encode('utf-8')).digest()

encryption.encrypt(key, "new.json")
