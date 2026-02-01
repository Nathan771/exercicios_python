def maior_num():
    lista = []
    for i in range(0, 5):
        num = float(input("Digite um número: "))
        lista.append(num)

    maior = max(lista)
    print(maior)

maior_num()