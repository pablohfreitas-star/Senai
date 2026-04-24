numero = int(input("Digite um número de até 3 dígitos: "))

centena = numero // 100
resto = numero % 100

dezena = resto // 10 // 1
unidade = resto % 10

print(f"CENTENA = {centena}")
print(f"DEZENA = {dezena}")
print(f"UNIDADE = {unidade}")