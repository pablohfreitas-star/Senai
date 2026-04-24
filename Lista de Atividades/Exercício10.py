x1 = float(input("x do primeiro ponto: "))
y1 = float(input("y do primeiro ponto: "))

x2 = float(input("x do segundo ponto: "))
y2 = float(input("y do segundo ponto: "))


distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"A distância entre os pontos é:", distancia)