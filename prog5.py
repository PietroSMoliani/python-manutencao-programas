#Problemas:

#Não usa random, número fixo.

#Seria melhor usar while para continuar tentando até acertar.
import random
numero = random.randint(1, 20)

palpite = int(input("Tente adivinhar o número: "))
while palpite != numero:
    if palpite > numero:
        print("Menor")
    else:
        print("Maior")
    palpite = int(input("Tente novamente: "))

print("Acertou!")
