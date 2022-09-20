print("PRIMERA PARTE")
print("Ingrese un Número:")
numerolf=int(input())
if numerolf == 0:
    print ("El número es cero")
elif numerolf < 0:
    print ("El número es negativo")
else:
    print ("El número es positivo")
print("SEGUNDA PARTE")
numeroWhile = int(input ("ingrese el número:"))
while numeroWhile<3:
    numeroWhile+=1
    print ("El nuevo número es "+ str(numeroWhile))
print("TERCERA PARTE")
numeroWhile = int(input ("ingrese el número:"))
while numeroWhile<3:
    numeroWhile+=1
    print ("El nuevo número es "+ str(numeroWhile))
print("CUARTA PARTE")
numeroFor = 0
for x in range(0,3):
    numeroFor+=1
    print (numeroFor)
    