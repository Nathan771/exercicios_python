def melhor_preco():
    produtos = []
    for i in range (0, 3):
        nome_produtos = input("Digite os produtos: ")
        preco = float(input("Digite o preço dos produtos: "))
        produtos.append({"Produto": nome_produtos, "Preço": preco:.2f})
    
    
    print(produtos)
    #menor = min(produto)
    #print(f"O menor produto custa: {menor}, sugiro comprar! ")
melhor_preco()