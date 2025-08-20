#Problema:

#A função não acumula corretamente (total = x sobrescreve, deveria somar).

Chamada está errada (resultado = soma_valores em vez de soma_valores(numeros)).
def soma_valores(lista):
    total = 0
    for x in lista:
        total += x
    return total

numeros = []
for i in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)

resultado = soma_valores(numeros)
print("Soma =", resultado)
