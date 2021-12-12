from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Fuente: https://pycryptodome.readthedocs.io/en/latest/src/public_key/dsa.html
# Se utiliza la misma libreria que en el caso de RSA. Necesario isntalarla.

# Se genera la clave privada y se escribe en fichero
key = DSA.generate(1024)    
f = open("public_key.pem", "w")
f.write(key.publickey().export_key().decode("utf-8"))
f.close()

# Se firma el mensaje mediante SHA
message = b"Hello"
hash_obj = SHA256.new(message)  #Hashea (encripta) el mensaje
signer = DSS.new(key, 'fips-186-3') #Se crea la firma y se firma el dicumento (juntar el hash del mensaje con la firma) --> documento final a enviar
signature = signer.sign(hash_obj)

# RECEPTOR:
# Abrir archivo y generar otra vez el hash
f = open("public_key.pem", "r")
hash_obj = SHA256.new(message)

pub_key = DSA.import_key(f.read())
verifier = DSS.new(pub_key, 'fips-186-3')

# Verificacion de la autenticidad del mesaje
try:
    verifier.verify(hash_obj, signature)
    print ("The message is authentic.")
except ValueError:
    print ("The message is not authentic.")