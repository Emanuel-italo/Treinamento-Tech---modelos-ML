def calcular_area():
    base = float(input("Digite o numero da base: "))
    altura = float(input("Digite o numero da altura: "))

    multiplicacao = base * altura
    
    return multiplicacao

retornando = calcular_area()
print(f"{retornando}")
