etanol = 4.90
gasolina = 5.80
combustivelSelecionado = (input("Informe G para gasolina e E para etanol: "))
valorSelecionado= float(input("Informe quantos litros deseja"))

valorPagamentoEtanol = etanol * valorSelecionado
valorPagamentoGasolina = gasolina * valorSelecionado

if combustivelSelecionado == "G":
    print(f"{valorPagamentoGasolina:.2f}")
elif combustivelSelecionado == "E":
    print(valorPagamentoEtanol)
