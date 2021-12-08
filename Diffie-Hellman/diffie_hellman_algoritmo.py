from random import randint

#Se establecen las variables en mayuscula como aqueellas conocidas por ambos usuarios
#Las siguientes variables (P, G) son conocidas por Javi y Unai
P = 23
G = 9   #base del exponente

print('Valor de P: %d'%P)
print('Valor de G: %d'%G)


#Javi escoge la clave privada j
j = 4
print('Clave privada de Javi: %d'%j)

#Y genera la nueva clave que posteriormente comparte con Unai
J = int(pow(G, j, P))


#Unai escoge la clave privada u y genera su clave que posteriormente comparte con Javi
u = 8
print('Clave privada de Unai: %d'%u)

U = int(pow(G, u, P))


#Una vez intercambiadas las claves, se determina la calve privada compartida
# Clave privada para Javi
key_javi = int(pow(U,j,P))
     
#Clave privada para Unai
key_unai = int(pow(J,u,P))

print('Clave Javi: %d'%key_javi)
print('Clave Unai: %d'%key_unai)


