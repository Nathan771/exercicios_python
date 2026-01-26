def maior_num_e_menor():
    lista = []
    for i in range(0, 3):
        num  = int(input("Digite o número: "))
        lista.append(num)  
    maior = max(lista)
    menor = min(lista)
    print(f"Maior número: {maior} ")
    print(f"Menor número: {menor} ")
maior_num_e_menor()