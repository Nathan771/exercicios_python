def validate():
    while True:
        try:
            num = int(input("Insira uma nota de 0 a 10: "))
            if num < 10 and num > 0:
                print(f"Nota validada! Nota selecionada: {num} ")
                break
            else:
                print("Insira uma nota válida! ")
                continue
        except ValueError:
            print("Insira apenas números! ")   
validate()