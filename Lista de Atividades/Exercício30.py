Salário_fixo = float(input("Digite o salário fixo: R$ "))
Vendas = float(input("Digite a quantidade de vendas: R$ "))

comissao = Vendas * 0.04
salario_final = Salário_fixo + comissao

print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário Final: R$ {salario_final:.2f}")