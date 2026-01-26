import time

def verificador():
    lista = []
    
    for i in range (0, 4):
        nota = float(input(f"Digite a {i+1} nota: "))
        lista.append(nota)

    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)


    if media >= 7:
       print("Aprovado!")
    else:
        print("Reprovado! Terá que fazer a prova final (A nota da prova final subsituira a menor nota do aluno.).")
        time.sleep(3)
        pf = float(input(f"Digite a nota da prova final: "))
        menornum = lista.index(min(lista))
        lista[menornum] = pf
        media = sum(lista) / len(lista)
    if media >= 7:
         print(f"Aprovado! A media desse aluno ficou: {media}")
    else:
        print("Reprovado! ")
verificador()