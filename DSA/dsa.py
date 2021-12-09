from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

#FUENTES:
#   Instalación de libreria (problemas de compatibilidad): https://stackoverflow.com/questions/58053316/how-to-fix-python-import-error-for-crypto-signature-dss
#       pip install pycripto
# https://pycryptodome.readthedocs.io/en/latest/src/public_key/dsa.html


message = b"Hello"
key = DSA.generate(1024)
h = SHA.new(message).digest()
k = random.StrongRandom().randint(1,key.q-1)
sig = key.sign(h,k)

if key.verify(h,sig):
    print("OK")
else:
    print("Incorrect signature")