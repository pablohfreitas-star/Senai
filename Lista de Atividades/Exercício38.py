Nascimento = int(input("Digite o ano de nascimento: "))
Ano_atual = int(input("Digite o ano atual: "))

anos = Ano_atual - Nascimento

meses = anos * 12
semanas = anos * 52
dias = anos * 365

print(f"--- Resultados ---")
print(f"Idade em anos: {anos} anos")
print(f"Idade em meses: {meses} meses")
print(f"Idade em semanas: {semanas} semanas")
print(f"Idade em dias: {dias} dias")