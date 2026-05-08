Quantidade_lata = int(input("Quantidade de latas (350 ml): "))
Quantidade_600 = int(input("Quantidade de garrafas (600 ml): "))
Quantidade_2l = int(input("Quantidade de garrafas (2 litros): "))

total_litros = (Quantidade_lata * 0.35) + (Quantidade_600 * 0.60) + (Quantidade_2l * 2.0)

print(f"\nO total de refrigerante comprado foi de: {total_litros:.2f} litros")