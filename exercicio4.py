# Item a: Números ímpares
impares = []
for numero in range(1,10,2):
    impares.append(numero)
print(impares) # 1, 3, 5, 7, 9

# Item b: Potência de 2
potenciaDe2 = []
for numero in range(1,8):
    potenciaDe2.append(2**numero)
print(potenciaDe2) # 2, 4, 8, 16, 32, 64, 128

# Item c: Números elevado ao quadrado
numerosAoquadrado = []
for numero in range(0,8):
    numerosAoquadrado.append(numero**2)
print(numerosAoquadrado) # 0, 1, 4, 9, 16, 25, 36, 49

# Item d: Números pares elevado ao quadrado
paresAoQuadrado = []
for numero in range(2,11,2):
    paresAoQuadrado.append(numero**2)
print(paresAoQuadrado) # 4, 16, 36, 64, 100

# Item e: Número somado ao seu anterior
somaDosAnteriores = []
for indice in range(0,7):
    if indice > 1:
        somaDosAnteriores.append(somaDosAnteriores[indice-2]+somaDosAnteriores[indice-1])
    else:
        somaDosAnteriores.append(1)
print(somaDosAnteriores) # 1, 1, 2, 3, 5, 8, 13

# Item f: Números que começa com a letra D - 2, 10, 12, 16, 17, 18, 19, 200
sequencia = []
for indice in range(0,8):
    match indice:
        case 0:
            sequencia.append(2)
        case 1:
            sequencia.append(sequencia[indice-1]+8)
        case 2:
            sequencia.append(sequencia[indice-1]+2)
        case 3:
            sequencia.append(sequencia[indice-1]+4)
        case 4:
            sequencia.append(sequencia[indice-1]+1)
        case 5:
            sequencia.append(sequencia[indice-1]+1)
        case 6:
            sequencia.append(sequencia[indice-1]+1)
        case 7:
            sequencia.append(sequencia[indice-1]+181)
print(sequencia) # 2, 10, 12, 16, 17, 18, 19, 200