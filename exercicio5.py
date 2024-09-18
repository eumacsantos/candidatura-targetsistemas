# Variável que será associação entre interruptores e as suas respectivas salas
interruptorSala = {}
# Variável que receberá a observação do estado da lâmpada
observacao = ""

# Informando os procedimentos antes da observação do estado da lâmpada
print("Primeira ida: Ligando o primeiro interruptor.")
print("Segunda ida: Ligando o segundo interruptor e desligando o primeiro.")

# Inserindo a observação do estado da lâmpada
while observacao != "ligada" and observacao != "desligada" and observacao != "quente":
    observacao = input("Digite o estado da lâmpada (ligada, desligada, quente): ")
    observacao = observacao.lower()

# Fazendo a associação de interruptores e salas de acordo com a observação
if observacao == "ligada":
    interruptorSala = {1: "B", 2: "A", 3: "C"}  
elif observacao == "desligada":
    interruptorSala = {1: "A", 2: "B", 3: "C"}
else:
    interruptorSala = {1: "B", 2: "C", 3: "A"}

# Imprimindo resultado
print(interruptorSala)