#Programa para calcular valor de pagamento de acordo com tipo do combustível e quantidade de litros
tipo = input("Digite o tipo abastecido 'E' para Etanol e 'G': ")
qlitros = float(input("Informe a quantidade de litros desejada: "))
#Declaração das váriaveis gasolina e etanol
vGaso = 5.80
vEta = 4.90
#Condição para entrar na gasolina ou etanol
if tipo == "G" or tipo == "g":
    valor = vGaso * qlitros
elif tipo == "E" or tipo == "e":
    valor = vEta * qlitros
else:
    print("Tipo inválido, informe E para Etanol ou G para gasolina")

print(f"{valor:.2f}")
