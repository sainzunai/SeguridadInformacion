from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto import Random


#cifrado de contraseña con AES!
data = b'contrasenya:3440'
key = b'ikerteniarazon11'
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

print("\n\nTexto cifrado con alogirtmo AES: ", ciphertext)
print("Pruba finalizada, generando firma digital y enviando...\n\n")


##########################

# Create a new RSA key
keyPAIR = RSA.generate(2048)
hash_obj_emisor = SHA256.new(ciphertext)
signature = pss.new(keyPAIR).sign(hash_obj_emisor)
# Load the public key
hash_obj_receptor = SHA256.new(ciphertext)
pub_key = keyPAIR.publickey()
verifier = pss.new(keyPAIR) # aqui el verificador es el correspondiente a PSS


try:
    verifier.verify(hash_obj_receptor, signature)
    print("Mensaje recibido y firma validada... Descifrando mensaje\n")
    descifrado = cipher.decrypt(ciphertext)
    print("Texto plano recibido: ", descifrado)
    
    
except ValueError:
    print("Mensaje recibido, credenciales de firma erroneas.")
