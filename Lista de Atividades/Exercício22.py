Moeda01 = int(input("Quantidade de moedas de 1 centavo: "))
Moeda05 = int(input("Quantidade de moedas de 5 centavos: "))
Moeda10 = int(input("Quantidade de moedas de 10 centavos: "))
Moeda25 = int(input("Quantidade de moedas de 25 centavos: "))
Moeda50 = int(input("Quantidade de moedas de 50 centavos: "))
Moeda1r = int(input("Quantidade de moedas de 1 real: "))

total = (Moeda01 * 0.01) + (Moeda05 * 0.05) + (Moeda10 * 0.10) + (Moeda25 * 0.25) + (Moeda50 * 0.50) + (Moeda1r * 1.00)

print(f"O valor total economizado é: R$ {total:.2f}")