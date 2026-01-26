def maior_num():
    lista = []
    for i in range(0, 3):
        num  = int(input("Digite o número: "))
        lista.append(num)  
    maior = max(lista)
    print(maior)
maior_num()