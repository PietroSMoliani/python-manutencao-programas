#input() retorna string, precisa converter para float ou int.

#O cálculo da média está errado porque está somando strings.

#Condições deveriam ser if ... elif ... else para evitar verificar duas vezes.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
