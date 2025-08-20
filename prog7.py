#Problema:

#continue faz loop infinito porque não incrementa i.
n = int(input("Digite um número: "))

i = 1
while i <= n:
    if i % 2 == 0:
        i += 1
        continue   
    print(i)
    i += 1
