digite_nota1 = float(input("Digite a primeira nota do aluno: "))
digite_nota2 = float(input("Digite a segunda nota do aluno: "))
digite_nota3 = float(input("Digite a terceira nota do aluno: "))



soma = digite_nota1 + digite_nota2 + digite_nota3

media = soma / 3


if media >=9:
    print("Excelente! Categoria A")
    
elif media == 7 and 8.9:
    print("Bom trabalho! Categoria B")
    

else:
    print("Precisa estudar mais. Categoria C")