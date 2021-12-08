from random import randint
#FUENTE: https://www.geeksforgeeks.org/implementation-diffie-hellman-algorithm/


#Se establecen las variables en mayuscula como aqueellas conocidas por ambos usuarios
#Las siguientes variables (P, G) son conocidas por Javi y Unai
P = 23  #numero primo
G = 9   #base del exponente

print("Se establecen los valores P y G para ambos usuarios. \nValor de P: %d; Valor de G: %d\n"%(P, G))



#Javi escoge la clave privada j
j = 4
print("(Clave privada de Javi j: %d)"%j)

#Y genera la nueva clave que posteriormente comparte con Unai
J = int(pow(G, j, P))


#Unai escoge la clave privada u y genera su clave que posteriormente comparte con Javi
u = 8
print("(Clave privada de Unai u: %d)"%u)

U = int(pow(G, u, P))

#Se cuela asier en la conversacion e intenta sacar la clave:
a = 2
A = int(pow(G, a, P))

#Intercambio de claves:
print("INTERCAMBIO DE CLAVES:")
print("\tJAVI: Hola Unai mi clave es J: %d" %J)
print("\tUNAI: Hola Javi, mi clave es U: %d" %U)

#Una vez intercambiadas las claves, se determina la calve privada compartida
# Clave privada para Javi
key_javi = int(pow(U,j,P))
     
#Clave privada para Unai
key_unai = int(pow(J,u,P))

key_asier = int(pow(U,a,P)) #es distinta --> solo funciona con 2 personas no con 3, asi que un MITM no sirve de nada.

print('Clave Javi key_javi: %d'%key_javi)
print('Clave Unai key_unai: %d'%key_unai)
print('Clave Unai key_asier: %d'%key_asier)
