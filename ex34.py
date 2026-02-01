def medias_calc():
    lista = []
    for i in range (0, 5):
        num = float(input("Digite os números: "))
        lista.append(num)
        
    soma = (sum(lista))
    media = (sum(lista) / len(lista))
    print(f"A soma dos números é: {soma} e a media é: {media}")

medias_calc()
