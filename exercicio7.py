agenda = {}

digite_nome_contato = input("Digite o nome do contato que deseja salvar: ")
digite_numero_contato = int(input("Digite o numero do contato: "))


agenda.update({digite_nome_contato:digite_numero_contato})


print(f"informações armazenadas no dicionarios são {agenda}")