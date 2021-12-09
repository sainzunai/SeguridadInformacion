#Se ha utilizado la libreria "pycryptodome" para hacer este programa
#Es necesario tenerla instalada.
#pip intall pycryptodome
#fuente: https://www.pythonpool.com/rsa-encryption-python/#:~:text=Report%20Ad-,What%20is%20RSA%20Encryption%20in%20python%3F,key%20and%20the%20private%20key.
#fuente 2: https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/asymmetric-key-ciphers/rsa-encrypt-decrypt-examples.html

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
 
keyPair = RSA.generate(1024)    #Se establecen los bits del codigo generado
 
pubKey = keyPair.publickey()
print(f"CLAVE PUBLICA:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")   #Imprimir la clave publica en formato hexadecimal
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
 
print(f"CLAVE PRIVADA: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")  #Imprimir la clave privada en formato hexadecimal
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
 
#encryption
msg = 'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg.encode()) #Mediante .encode() se convierte el string msg a bytes
print("MENSAJE ENCRIPTADO:", binascii.hexlify(encrypted))

#desencriptacion
#decMessage = encryptor.decrypt(encrypted, privKeyPEM).decode()
#print("MENSAJE DESENCRIPTADO:", binascii.hexlify(decMessage))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)
