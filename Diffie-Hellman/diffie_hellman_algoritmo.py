from random import randint

#Se establecen las variables en mayuscula como aqueellas conocidas por ambos usuarios
#Las siguientes variables (P, G) son conocidas por Javi y Unai
P = 23
G = 9   #base del exponente

print("Se establecen los valores P y G para ambos usuarios. \nValor de P: %d; Valor de G: %d\n"%(P, G))



#Javi escoge la clave privada j
j = 4
print('Clave privada de Javi j: %d'%j)

#Y genera la nueva clave que posteriormente comparte con Unai
J = int(pow(G, j, P))


#Unai escoge la clave privada u y genera su clave que posteriormente comparte con Javi
u = 8
print('Clave privada de Unai u: %d'%u)

U = int(pow(G, u, P))

#Intercambio de claves:
print("JAVI: Hola Unai mi clave es J: %d" %J)
print("UNAI: Hola Javi, mi clave es U: %d" %U)

#Una vez intercambiadas las claves, se determina la calve privada compartida
# Clave privada para Javi
key_javi = int(pow(U,j,P))
     
#Clave privada para Unai
key_unai = int(pow(J,u,P))

print('Clave Javi key_javi: %d'%key_javi)
print('Clave Unai key_unai: %d'%key_unai)
