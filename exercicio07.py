nometime1 =input("Qual nome do primeiro time?:")
nometime2 =input("Qual nome do segundo time?:")
time1 = int(input(f"Quantos gols o {nometime1} fez?"))
time2 = int(input(f"Quantos gols o {nometime2} fez?"))
if time1 > time2:
    print(f" {nometime1} é vencedor da partida")
else:
    if time1 == time2:
        print("Os times empataram")
    else:
        print(f" {nometime2} é vencedor da partida")
