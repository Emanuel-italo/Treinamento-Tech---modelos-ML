lista = []

while True:
    digite_numero = int(input("Digite um numero: "))

    if digite_numero == 0:
        print("Você parou de adicionar coisas na lista...")
        print(f"Números inseridos na lista são: {lista}")
        soma = sum(lista)
        print(f"o resultado total dos numeros inseridos na lista são {soma}")
        break

    lista.append(digite_numero)

        