# Inicialização das variáveis necessárias para resolução do problema
interruptorSala = {}
interruptores = [1,2,3]
salas = ["A","B","C"]
opcoesDeEstado = ["quente","ligada","desligada"]
observacao = ""

# Informando os procedimentos, antes da observação do estado da lâmpada na sala A
print("Ligando o primeiro interruptor.")
print("Esperando 5 minutos")
print("Desligando o primeiro e ligando o segundo interruptor")
print("Entrando na sala A.")

# Inserindo a observação do estado da lâmpada da sala A
while not(observacao in opcoesDeEstado):
    observacao = input("Digite o estado da lâmpada (ligada, desligada ou quente): ")
    observacao = observacao.lower()

# Descobrindo o interruptor correto da sala A, de acordo com a observação feita
for estado in opcoesDeEstado:
    if observacao == estado:
        interruptorSala[interruptores[opcoesDeEstado.index(observacao)]] = salas[0]
        interruptores.pop(opcoesDeEstado.index(observacao))
        salas.pop(0)
        opcoesDeEstado.remove("quente")
        break

# Informando os procedimentos, antes da última ida permitida, na qual será na sala B
print("Sainda da sala A e desligando o segundo interruptor.")
print("Ligando o primeiro interruptor entre os interruptores restante.")
print("Entrando na sala B.")

# Inserindo a observação do estado da lâmpada da sala B
observacao = ""
while not(observacao in opcoesDeEstado):
    observacao = input("Digite o estado da lâmpada (ligada ou desligada): ")
    observacao = observacao.lower()

# Descobrindo o interruptor correto da sala B, de acordo com a observação feita
if observacao == "ligada":
    interruptorSala[interruptores[0]] = salas[0]
    interruptores.pop(0)
    salas.pop(0)
else:
    interruptorSala[interruptores[0]] = salas[1]
    interruptores.pop(0)
    salas.pop(1)

# Associando a sala C com o último interruptor
interruptorSala[interruptores[0]] = salas[0]

# Imprimindo resultado
print(interruptorSala)