n1 =float(input("Qual é a primeira nota?:"))
n2 =float(input("Qual é a segunda nota?:"))
n3 =float(input("Qual é a terceira nota?:"))
media = float(n1 + n2 + n3) / 3
print(f"A média desse aluno é: {media}")
if media >= 7:
    print("aluno aprovado")
else:
    print("aluno reprovado")
