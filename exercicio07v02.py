tipo = input("Digite o tipo abastecido 'E' para Etanol e 'G': ")

qlitros = float(input("Informe a quantidade de litros desejada: "))

vGaso = 5.80
vEta = 4.90

if tipo == "G":
    valor = vGaso * qlitros
else:
    valor = vEta * qlitros

print(f"{valor:.2f}")
