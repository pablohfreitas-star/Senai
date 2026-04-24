quant_pão = int(input("Digite quantos pães foi vendido: "))
quant_broa = int(input("digite quantas broas foi vendida: "))

arrecadado = (quant_pão * 0.12) + (quant_broa * 1.50)
poupança = ( arrecadado * 0.10)

print("total de vendas de pão e broas foi: ", arrecadado )
print("quantidade de dinheiro que ira para poupança:", poupança)