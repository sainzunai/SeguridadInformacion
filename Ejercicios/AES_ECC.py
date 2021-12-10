from Crypto.Cipher import AES
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256


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
    
# Create a new ECC key
key = ECC.generate(curve = 'P-256')
hash_obj_emisor = SHA256.new(ciphertext)
signer = DSS.new(key, 'fips-186-3') #certificado estandar para firmas digitales
signature = signer.sign(hash_obj_emisor)
# Load the public key
hash_obj_receptor = SHA256.new(ciphertext)
verifier = DSS.new(key, 'fips-186-3')


try:
    verifier.verify(hash_obj_receptor, signature)
    print("Mensaje recibido y firma validada... Descifrando mensaje\n")
    descifrado = cipher.decrypt(ciphertext)
    print("Texto plano recibido: ", descifrado)
    
    
except ValueError:
    print("Mensaje recibido, credenciales de firma erroneas.")

