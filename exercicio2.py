# Recebendo a string
caracteres = input("Digite a string de sua preferência: ")
# Colocando todas as letras da string em minúsculas
caracteres = caracteres.lower()

# Primeira opção de resposta utilizando função do Python
ocorrencia = 0
ocorrencia = caracteres.count("a")

# Segunda opção de resposta utilizando FOR para percorrer a string (lista de caracteres) e verificar a quantidade de vezes que a letra 'a' aparece
ocorrencia = 0
for letra in caracteres:
    if letra == "a":
        ocorrencia += 1

# Imprimindo o número de vezes que a letra 'a' apareceu na string
print(ocorrencia)