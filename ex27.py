def melhor_preco():
    produtos = []
    for i in range (0, 3):
        nome_produtos = input("Digite os produtos: ")
        preco = float(input("Digite o preço dos produtos: "))
        produtos.append({
                
                "Produto": nome_produtos, 
                "Preço": f"{preco:.2f}" 
                
                })
    
    menor = min(produtos, key=lambda u: u["Preço"])
    print(f"O menor preço é {menor['Preço']} ")
    
melhor_preco()