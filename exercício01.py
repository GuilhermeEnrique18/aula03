nome = input("Informe seu nome: ")
#idade = int(input("Informe sua idade: "))

salario = float(input("Informe seu salário: "))
percentualAumento = float(input("Informe o percentual de aumento desejado: "))
caculoPercentual = (salario * percentualAumento) / 100
salarioTotal = salario + caculoPercentual

print(f"Olá {nome}! \n "
      f"Seu salário é: R${salario:.2f} \n"
      f" você terá R${caculoPercentual:.2f} de aumento \n"
      f" Seu novo salário é: R${salarioTotal:.2f}")

