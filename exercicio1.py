# Recebendo o número para verificação
numero = int(input("Digite um número: "))
anterior = 0
sucessor = 1

# Calculando a sequência de Fibonacci
while sucessor < numero:
    sucessor += anterior
    anterior = sucessor - anterior

# Verificando se o número digitado pertence a lista ou não e imprimindo o resultado da verificação
if sucessor == numero:
    print("O número " + str(numero) + " pertence a sequência de Fibonacci.")
else:
    print("O número " + str(numero) + " NÃO pertence a sequência de Fibonacci.")