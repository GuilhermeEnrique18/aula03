print("Bem vindo ao calculo de média!")

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
media = (n1 + n2 + n3) / 3

if media >= 7:
    print(f"Aprovado! Sua média foi {media}")
else:
    if media < 4:
        print(f"Reprovado!Sua média foi {media}")
    else:
        print(f"Recuperação!Sua média foi {media}")
