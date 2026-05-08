altura_pessoa = float(input("Digite sua altura (em metros): "))
sombra_pessoa = float(input("Digite o tamanho da sua sombra (em metros): "))
sombra_predio = float(input("Digite o tamanho da sombra do prédio (em metros): "))


altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa


print(f"A altura do prédio é: {altura_predio:} metros")