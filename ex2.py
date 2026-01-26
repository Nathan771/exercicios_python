
def notas():
        try:
        
            num = float(input("Digite a primeira nota: "))
            num2 = float(input("Digite a segunda nota: "))
            num3 = float(input("Digite a terceira nota: "))
            num4 = float(input("Digite a quarta nota: "))


            lista = [num, num2, num3, num4]


            maior = max(lista)
            menor = min(lista)

            media = sum(lista) / 4

            print(f"A maior nota é ({maior}))")
            print(f"A menor nota é ({menor}))")
            print(f"A média das notas é: ({media}))")
        
        except ValueError:
            print("Digite apenas números! ")
notas()