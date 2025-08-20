#Problemas:

#A ordem está errada — começa com notas de 1, deveria começar com notas maiores.

Operações devem ser feitas de cima para baixo (100 → 1).
valor = int(input("Digite o valor: "))

notas100 = valor // 100
valor %= 100

notas50 = valor // 50
valor %= 50

notas20 = valor // 20
valor %= 20

notas10 = valor // 10
valor %= 10

notas5 = valor // 5
valor %= 5

notas2 = valor // 2
valor %= 2

notas1 = valor // 1
valor %= 1

print("100:", notas100)
print("50 :", notas50)
print("20 :", notas20)
print("10 :", notas10)
print("5  :", notas5)
print("2  :", notas2)
print("1  :", notas1)
