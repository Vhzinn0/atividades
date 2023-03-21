lista_de_compras = []

while True:
    
    print("Escolha uma opção:\n1 - Adicionar item\n2 - Remover item\n3 - Listar itens\n4 - Sair")
    opcao = input("Opção escolhida: ")

    if opcao == "1":
        
        item = input("Digite o nome do item a ser adicionado: ")
        lista_de_compras.append(item)
        print(f"O item {item} foi adicionado à lista.")

    elif opcao == "2":
        
        item = input("Digite o nome do item a ser removido: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"O item {item} foi removido da lista.")
        else:
            print(f"O item {item} não está na lista.")

    elif opcao == "3":
        
        print("Itens na lista:")
        for item in lista_de_compras:
            print(item)

    elif opcao == "4":
        
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")