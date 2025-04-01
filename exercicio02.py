n1 = float(input("Digite n1: "))
n2 = float(input("Digite n2: "))
operacaoSolicitada = input("Digite o símbolo de uma das quatro operaçôes matemáticas desejada: ")

soma = n1 + n2
subtracao = n1 - n2
divisao = n1 / n2
multiplicacao = n1 * n2

"""print(f"Soma: {soma} \n"
      f" Subtração: {subtracao} \n"
      f" Divisão: {divisao} \n"
      f" Multiplicação: {multiplicacao}")"""

if operacaoSolicitada == "+" :
    print(soma)
elif operacaoSolicitada == "-":
    print(subtracao)
elif operacaoSolicitada == "/":
    print(divisao)
elif operacaoSolicitada == "*":
    print(multiplicacao)