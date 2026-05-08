horas_normais = float(input("Digite a quantidade de horas normais: "))
horas_extras = float(input("Digite a quantidade de horas extras: "))

valor_horas_normais = horas_normais * 10
valor_horas_extras = horas_extras * 15
salario_bruto = valor_horas_normais + valor_horas_extras
imposto = salario_bruto * 0.10
salario_liquido = salario_bruto - imposto

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")