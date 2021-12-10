from Crypto.Cipher import AES
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

#Este ejercicio combina el cirfrado AES con la técnica de firma digital DSA, para asegurar un envío de datos seguro e inmodificable.

# EMISOR:

# Informacion a enviar
data = b'contrasenya:3440'

# Mi clave de cifrado AES
key = b'ikerteniarazon11'

# CRIFRADO: Se genera el objeto que va a cefrar y se cifra el mensaje mediante la clave
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce    # Parámetro que deja rastro cuando se desencripta el mensaje, para que solo se pueda abrir una vez (rompe la llave al arirlo)
ciphertext, tag = cipher.encrypt_and_digest(data)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

print("\n\nTexto cifrado con alogirtmo AES: ", ciphertext)
print("Pruba finalizada, generando firma digital y enviando...\n\n")

    
# Crea clave DSA y lo firma
keyPAIR = DSA.generate(2048)
hash_obj_emisor = SHA256.new(ciphertext)
signer = DSS.new(keyPAIR, 'fips-186-3') # DSS es la certifcacion para implementar DSS --> Digital Signature Services
signature = signer.sign(hash_obj_emisor)


# RECEPTOR:

# Descifrado del mensaje
hash_obj_receptor = SHA256.new(ciphertext)
pub_key = keyPAIR.publickey()
verifier = DSS.new(pub_key, 'fips-186-3')


# Verificación de que el mensaje se corresponde con el autor y/o no se ha alterado
try:
    verifier.verify(hash_obj_receptor, signature)
    print("Mensaje recibido y firma validada... Descifrando mensaje\n")
    descifrado = cipher.decrypt(ciphertext)
    print("Texto plano recibido: ", descifrado)
    
    
except ValueError:
    print("Mensaje recibido, credenciales de firma erroneas.")

