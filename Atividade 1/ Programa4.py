contador = 1
soma_notas = 0

while contador <= 4:
    notas = float(input(f"digite a nota do { contador } bimestre")) 
    if nota < 0 or nota > 10:
        print("nota invalida. A nota deve estar entre 0 e 10")
        continue
    contador += 1
    soma_notas += nota

media = soma_notas / 4
print("a media de notas e: ", media)

if media >= 7:
    print("O aluno esta aprovado")

if media >= 5:
    print("O aluno esta em recuperaçao")

else:
     print("O aluno esta reprovado")

