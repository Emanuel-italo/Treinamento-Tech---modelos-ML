def calculando():
    try:
        digite_dividendo = int(input("Digite o numero para ser o dividendo: \n"))
        digite_divisor = int(input("digite o numero para ser o divisor: \n"))
        
        resultado = digite_dividendo/digite_divisor
        
        return resultado
        
    except ZeroDivisionError:
        print("Não pode dividir por zero!!")
        return None
    
    except Exception:
        print("Você precisa digitar apenas números!")
        return None
    

chamando = calculando()
print(f"chamando a função da divisão {chamando}")