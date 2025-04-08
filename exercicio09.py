desejaContinuar = "1"
while desejaContinuar == "1" :
    mesDesejado = int(input("Digite um número de 1 a 12 para saber o mês: "))

    match mesDesejado:
        case 1:
            print("janeiro")
        case 2:
            print("fevereiro")
        case 3:
            print("março")
        case 4:
            print("abril")
        case 5:
            print("maio")
        case 6:
            print("junho")
        case 7:
            print("julho")
        case 8:
            print("agosto")
        case 9:
            print("setembro")
        case 10:
            print("outubro")
        case 11:
            print("novembro")
        case 12:
            print("dezembro")
        case _:
            print("Número invalido")

    desejaContinuar = input("Digite 1 para continuar ou qualquer tecla para encerrar: ")

print("P R O G R A M A - E N C E R R A D O")