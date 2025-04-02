abastecer = input("O que você vai abastecer? Digite G para gasolina ou E para etanol:")
litros = float(input("Quantos litros você vai abastecer?"))

valG = 5.8
valE = 4.9

if abastecer == "G" or abastecer == "g" :
    valorG = litros * valG
    print(f"total a pagar de gasolina: {valorG:.2f}")
elif abastecer == "E" or abastecer == "e" :
    valorE = litros * valE
    print(f"total a pagar de etanol: {valorE:.2f}")
else:
    print(f"tipo de combustível inválido")

