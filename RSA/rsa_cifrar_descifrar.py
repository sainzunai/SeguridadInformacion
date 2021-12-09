import random

def gcd(a, b):  
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi): #algoritmo de euclides inverso, para generar el elemento del par de clave privada.
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

# Comprobación de si es primo

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


# Genereamos las claves por definicion, comprobando si es primo o no 
def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Los dos numeros tienen que ser primos')
    elif p == q:
        raise ValueError('p y q no pueden ser iguales')
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):

    key, n = pk
    # a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):

    key, n = pk
    #a^b mod m
    aux = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


if __name__ == '__main__':


    print("===========================================================================================================")
    print("=============================== RSA Encriptador / Desencriptador ==========================================")
    print(" ")

    p = int(input(" - Introduce un numero primo (17, 19, 23, etc): "))
    q = int(input(" - Introduce otro numero primo (Diferente al anterior): "))

    print(" - Generando clave publica/privada . . .")

    public, private = generate_key_pair(p, q)

    print(" - Tu clave publica es ", public, " y tu clave privada es ", private)

    message = input(" - Introduzca mensaje a cifrar: ")
    encrypted_msg = encrypt(public, message)

    print(" - Tu mensaje cifrado es: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print(" - Descifrando el mensaje con la clave privada ", private, " . . .")
    print(" - Tu mensaje descifrado: ", decrypt(private, encrypted_msg))

    print(" ")
    print("============================================ FIN ==========================================================")
    print("===========================================================================================================")