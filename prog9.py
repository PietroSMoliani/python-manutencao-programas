#Funciona corretamente, mas pode aceitar maiúsculas:
palavra = input("Digite uma palavra: ").lower()

vogais = 0
for letra in palavra:
    if letra in "aeiou":
        vogais += 1

print("Quantidade de vogais:", vogais)
