nomeTimeUm = input("Informe o nome do time: ")
golsTimeUm = int(input(f"Informe a quantidade de gols marcado pelo {nomeTimeUm} na partida: "))

nomeTimeDois = input("Informe o nome do time: ")
golsTimeDois = int(input(f"Informe a quantidade de gols marcado pelo {nomeTimeDois} na partida: "))


if golsTimeUm > golsTimeDois:
    print(f"{nomeTimeUm} Venceu! O {nomeTimeDois} é uma desgraça!")
elif golsTimeUm == golsTimeDois:
    print("Empate!")
else:
    print(f"{nomeTimeDois} Venceu! O {nomeTimeUm} é uma desgraça!")