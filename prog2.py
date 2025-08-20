#Problemas:

#Condição if i <= 2 imprime só até 2, mas não atende a ideia de imprimir todos menores que n.

#Corrigindo para imprimir todos os números de 0 até n-1.
n = int(input("Digite um número: "))
i = 0
while i < n:
    print(i)
    i += 1
